<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class UserController extends Controller
{
    /**
     * Display a list of product that user love.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function loveProducts()
    {
        $user = auth()->user();
        if (!$user) {
            return response()->json([
                'status' => 'error',
                'message' => 'User not found',
            ], 404);
        }

        $products = $user->loveProducts()->with('thumbnail')->get();

        return response()->json($products);
    }

    public function cartProducts()
    {
        $user = auth()->user();

        if (!$user) {
            return response()->json([
                'status' => 'error',
                'message' => 'User not found',
            ], 404);
        }

        $products  = $user->cartProducts()->with('thumbnail')->get();

        return response()->json($products);
    }

    public function toggleLoveProduct(Request $request)
    {
        $validator = Validator::make([
            'product_id' => 'required|integer',
        ], $request->all());

        if ($validator->fails()) {
            return response()->json([
                'message' => 'Validation error',
                'errors' => $validator->errors(),
            ], 422);
        }

        $user = auth()->user();

        $user->loveProducts()->toggle($request->product_id);

        return response()->json([
            'message' => 'Toggle love product successfully',
        ], 200);
    }

    public function addToCart(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'product_id' => 'required|integer',
            'quantity' => 'required|integer|min:1',
            'size' => 'nullable|integer',
        ]);

        if ($validator->fails()) {
            return response()->json([
                'message' => 'Validation error',
                'errors' => $validator->errors(),
            ], 422);
        }

        $user = auth()->user();

        if (!$user) {
            return response()->json([
                'message' => 'User not found',
            ], 404);
        }

        // if product is already in cart with the same size, increase the quantity, otherwise create a new cart item
        $cartItem = $user->cartProducts()
            ->where('product_id', $request->product_id)
            ->where('size', $request->size)
            ->first();
        if ($cartItem) {
            $cartItem->pivot->quantity += $request->quantity;
            $cartItem->pivot->save();
            $cartItem->save();
        } else {
            $user->cartProducts()->attach($request->product_id, [
                'quantity' => $request->quantity,
                'size' => $request->size,
            ]);
        }

        return response()->json([
            'message' => 'Add to cart successfully',
        ], 200);
    }

    public function removeFromCart(Request $request)
    {
        $user = auth()->user();
        if (!$user) {
            return response()->json([
                'message' => 'User not found',
            ], 404);
        }

        if (!$user->cartProducts()->where('product_id', $request->product_id)->exists()) {
            return response()->json([
                'message' => 'Product not found in cart',
            ], 404);
        }

        if ($request->size) {
            $user->cartProducts()->where('product_id', $request->product_id)->where('size', $request->size)->detach();
        } else {
            $user->cartProducts()->where('product_id', $request->product_id)->detach();
        }

        return response()->json([
            'message' => 'Remove from cart successfully',
        ], 200);
    }

    public function updateCartPivot(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'quantity' => 'nullable|integer|min:1',
            'size' => 'nullable|integer|min:1',
            'old_size' => 'nullable|integer|min:1',
        ]);

        if ($validator->fails()) {
            return response()->json([
                'message' => 'Validation error',
                'errors' => $validator->errors(),
            ], 422);
        }

        $user = auth()->user();

        if (!$user) {
            return response()->json([
                'message' => 'User not found',
            ], 404);
        }

        if (!$user->cartProducts()->where('product_id', $request->product_id)->exists()) {
            return response()->json([
                'message' => 'Product not found in cart',
            ], 404);
        }

        // if request->old_size, find the cart item with the old size and update it
        $cartItem = null;
        if ($request->old_size) {
            $cartItem = $user->cartProducts()->where('product_id', $request->product_id)->where('size', $request->old_size)->first();
        } else {
            $cartItem = $user->cartProducts()->where('product_id', $request->product_id)->first();
        }

        if (!$cartItem) {
            return response()->json([
                'message' => 'Cart item not found',
            ], 404);
        }

        if ($request->quantity) {
            $cartItem->pivot->quantity = $request->quantity;
            $cartItem->pivot->save();
        }

        // check if the new size is already in cart, if so, merge the quantity
        if ($request->size && $user->cartProducts()->where('product_id', $request->product_id)->where('size', $request->size)->exists()) {
            $newCartItem = $user->cartProducts()->where('product_id', $request->product_id)->where('size', $request->size)->first();
            $newCartItem->pivot->quantity += $cartItem->pivot->quantity;
            $newCartItem->pivot->save();
            $cartItem->pivot->delete();
        } elseif ($request->size) {
            $cartItem->pivot->size = $request->size;
            $cartItem->pivot->save();
        }

        return response()->json([
            'message' => 'Change cart item quantity successfully',
        ], 200);
    }

    public function clearCart(Request $request)
    {
        $user = auth()->user();

        if (!$user) {
            return response()->json([
                'message' => 'User not found',
            ], 404);
        }

        $user->cartProducts()->detach();

        return response()->json([
            'message' => 'Clear cart successfully',
        ], 200);
    }
}
