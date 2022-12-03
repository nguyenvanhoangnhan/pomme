<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Models\Clothes;
use App\Models\Product;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class ClothesController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function index()
    {
        // return shoes with product data inside
        return response()->json(Clothes::with('product.thumbnail')->get());
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function store(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'name' => 'required',
            'price' => 'required|min:0',
            'discount_percent' => 'nullable|min:0|max:100',
            'in_stock' => 'nullable|min:0',
            'category' => 'required|string',
        ]);

        if ($validator->fails()) {
            return response()->json([
                'success' => false,
                'message' => 'Validation Error.',
                'errors' => $validator->errors(),
            ], 400);
        }

        $product = Product::create([
            'name' => $request->name,
            'price' => $request->price,
            'discount_percent' => $request->discount_percent ? $request->discount_percent : 0,
            'in_stock' => $request->in_stock ? $request->in_stock : 0,
            'type' => 'clothes',
        ]);

        if (!$product) {
            return response()->json([
                'success' => false,
                'message' => 'Product could not be created',
            ], 500);
        }

        $clothes = Clothes::create([
            'product_id' => $product->id,
            'category' => $request->category,
        ]);

        return response()->json([
            'success' => true,
            'message' => 'Clothes created successfully.',
            'data' => $clothes->with('product'),
        ]);
    }

    /**
     * Display the specified resource using product_id.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function show(Request $request)
    {
        $clothes = Clothes::with('product.images')->where('product_id', $request->product_id)->first();
        if (!$clothes) {
            return response()->json([
                'success' => false,
                'message' => 'Clothes not found',
            ], 400);
        }

        return response()->json($clothes);
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Shoe  $shoe
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'clothes_id' => 'required|exists:clothes,id',
            'name' => 'nullable',
            'price' => 'nullable|min:0',
            'discount_percent' => 'nullable|min:0|max:100',
            'in_stock' => 'nullable|min:0',
            'category' => 'nullable|string',
        ]);

        if ($validator->fails()) {
            return response()->json([
                'success' => false,
                'message' => 'Validation Error.',
                'errors' => $validator->errors(),
            ], 400);
        }

        $clothes = Clothes::find($request->clothes_id);
        $product = Product::find($clothes->product_id);
        if ($request->name) {
            $product->name = $request->name;
        }

        if ($request->price) {
            $product->price = $request->price;
        }

        if ($request->discount_percent) {
            $product->discount_percent = $request->discount_percent;
        }

        if ($request->in_stock) {
            $product->in_stock = $request->in_stock;
        }

        if ($request->category) {
            $clothes->category = $request->category;
        }

        $product->save();
        $clothes->save();
        $clothes = Clothes::with('product')->find($request->clothes_id);

        return response()->json($clothes, 202);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Clothes  $clothes
     * @return \Illuminate\Http\JsonResponse
     */
    public function destroy(Clothes $clothes)
    {
    }
}
