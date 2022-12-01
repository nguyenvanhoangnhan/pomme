<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
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
        $products = $user->loveProducts()->get();

        return response()->json($products);
    }

    public function cartProducts()
    {
        $user = auth()->user();
        // with pivot quantity and size
        $products  = $user->cartProducts()->get();

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
        $validator = Validator::make([
            'product_id' => 'required|integer',
            'quantity' => 'required|integer|min:1',
            'size' => 'nullable|integer',
        ], $request->all());

        if ($validator->fails()) {
            return response()->json([
                'message' => 'Validation error',
                'errors' => $validator->errors(),
            ], 422);
        }

        $user = auth()->user();

        $user->cartProducts()->attach($request->product_id, [
            'quantity' => $request->quantity,
            'size' => $request->size,
        ]);

        return response()->json([
            'message' => 'Add to cart successfully',
        ], 200);
    }

    public function removeFromCart(Request $request)
    {
        $user = auth()->user();

        $user->cartProducts()->detach($request->product_id);

        return response()->json([
            'message' => 'Remove from cart successfully',
        ], 200);
    }

    public function updateCartPivot(Request $request)
    {
        $validator = Validator::make([
            'quantity' => 'nullable|integer|min:1',
            'size' => 'nullable|integer|min:1',
        ], $request->all());

        if ($validator->fails()) {
            return response()->json([
                'message' => 'Validation error',
                'errors' => $validator->errors(),
            ], 422);
        }

        $user = auth()->user();
        if ($request->quantity) {
            $user->cartProducts()->updateExistingPivot($request->product_id, [
                'quantity' => $request->quantity,
            ]);
        }

        if ($request->size) {
            $user->cartProducts()->updateExistingPivot($request->product_id, [
                'size' => $request->size,
            ]);
        }

        return response()->json([
            'message' => 'Change cart item quantity successfully',
        ], 200);
    }
}
