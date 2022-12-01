<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Models\Product;
use App\Models\Shoe;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class ShoeController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\JsonResponse
     */
    public function index()
    {
        // return shoes with product data inside, product has thumbnail inside
        return response()->json(Shoe::with('product.thumbnail')->get());
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'name' => 'required',
            'price' => 'required|min:0',
            'discount_percent' => 'nullable|min:0|max:100',
            'in_stock' => 'nullable|min:0',
            'gender' => 'required|in:0,1,2',
            'series' => 'required',
            'shape' => 'required|numeric',
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
            'type' => 'shoe',
        ]);

        if (!$product) {
            return response()->json([
                'success' => false,
                'message' => 'Product could not be created',
            ], 500);
        }

        $shoe = Shoe::create([
            'product_id' => $product->id,
            'gender' => $request->gender,
            'series' => $request->series,
            'shape' => $request->shape,
        ]);

        return response()->json([
            'success' => true,
            'message' => 'Shoe created successfully.',
            'data' => $shoe->with('product'),
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
        return response()->json(Shoe::with('product.images', 'children')->where('product_id', $request->product_id)->get());
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Shoe  $shoe
     * @return \Illuminate\Http\Response
     */
    public function edit(Shoe $shoe)
    {
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Shoe  $shoe
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Shoe $shoe)
    {
        $validator = Validator::make([
            'product_id' => $request->product_id,
            'name' => 'nullable',
            'price' => 'nullable|min:0',
            'discount_percent' => 'nullable|min:0|max:100',
            'in_stock' => 'nullable|min:0',
            'gender' => 'nullable|in:0,1,2',
            'series' => 'nullable',
            'shape' => 'nullable|numeric',
        ], $request->all());

        if ($validator->fails()) {
            return response()->json([
                'success' => false,
                'message' => 'Validation Error.',
                'errors' => $validator->errors(),
            ], 400);
        }

        $product = Product::find($shoe->product_id);
        $shoe = Shoe::where('product_id', $request->product_id)->first();
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

        if ($request->gender) {
            $shoe->gender = $request->gender;
        }

        if ($request->series) {
            $shoe->series = $request->series;
        }

        if ($request->shape) {
            $shoe->shape = $request->shape;
        }

        $product->save();
        $shoe->save();
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function destroy(Request $request)
    {
    }

    public function children(Request $request)
    {
        $request->validate([
            'shoe_id' => 'required|integer',
        ]);
        $shoe = Shoe::find($request->shoe_id);

        return response()->json($shoe->children);
    }
}
