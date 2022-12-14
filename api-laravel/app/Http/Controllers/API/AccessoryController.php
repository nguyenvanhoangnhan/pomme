<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Models\Accessory;
use App\Models\Product;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class AccessoryController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function index()
    {
        // return shoes with product data inside
        return response()->json(Accessory::with('product.thumbnail')->get());
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
            'thumbnail' => 'required|string',
            'images' => 'required|array|min:3',
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
            'type' => 'accessory',
        ]);

        if (!$product) {
            return response()->json([
                'success' => false,
                'message' => 'Product could not be created',
            ], 500);
        }

        $accessory = Accessory::create([
            'product_id' => $product->id,
            'category' => $request->category,
        ]);

        $product->thumbnail()->create([
            'url' => $thumbnail,
            'is_thumbnail' => true,
        ]);

        foreach ($images as $image) {
            $product->images()->create([
                'url' => $image,
                'is_thumbnail' => false,
            ]);
        }

        return response()->json([
            'success' => true,
            'message' => 'Acessory created successfully.',
            'data' => $accessory->with('product'),
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
        $accessory = Accessory::with('product.images')->where('product_id', $request->product_id)->first();
        if (!$accessory) {
            return response()->json([
                'success' => false,
                'message' => 'Accessory not found',
            ], 400);
        }

        return response()->json($accessory);
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
            'accessory_id' => 'required|exists:accessories,id',
            'name' => 'nullable',
            'price' => 'nullable|min:0',
            'discount_percent' => 'nullable|min:0|max:100',
            'thumbnail' => 'nullable|string',
            'images' => 'nullable|array|min:3',
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

        $accessory = Accessory::find($request->accessory_id);
        $product = Product::find($accessory->product_id);
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
            $accessory->category = $request->category;
        }

        if ($request->thumbnail) {
            $product->thumbnail()->update([
                'url' => $request->thumbnail,
            ]);
        }

        if ($request->images) {
            $product->images()->where('is_thumbnail', false)->delete();
            foreach ($request->images as $image) {
                $product->images()->create([
                    'url' => $image,
                    'is_thumbnail' => false,
                ]);
            }
        }

        $product->save();
        $accessory->save();
        $accessory = Accessory::with('product')->find($request->accessory_id);

        return response()->json($accessory, 202);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Accessory  $accessory
     * @return \Illuminate\Http\JsonResponse
     */
    public function destroy(Accessory $accessory)
    {
    }
}
