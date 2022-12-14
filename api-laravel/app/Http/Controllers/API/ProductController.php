<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Models\Product;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Http\Request;

class ProductController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @param \Illuminate\Http\Request $request
     * @return \Illuminate\Http\Response
     */
    public function index(Request $request)
    {
        $priceSort = $request->has('price_sort') ? strtoupper($request->price_sort) : 'default';
        $products = Product::with('thumbnail');
        if ($priceSort === 'ASC' || $priceSort === 'DESC') {
            $products = $products->orderBy('price', $priceSort);
        }

        $sale = $request->has('sale') ? $request->sale : false;
        if ($sale) {
            $products = $products->where('discount_percent', '>', 0);
        }

        $type = $request->has('type') ? strtoupper($request->type) : false;
        if ($type === 'SHOE') {
            $products = $products->where('type', $type);
            $products = $this->filterShoe($products, $request);
        }

        if ($type === 'CLOTHES') {
                $products = $products->where('type', $type);
                $products = $this->filterClothes($products, $request);
        }

        if ($type === 'ACCESSORY') {
            $products = $products->where('type', $type);
            $products = $this->filterAccessory($products, $request);
        }

        return response()->json($products->paginate(12));
    }

    /**
     * Filter the shoe products based on the request and return the filtered products
     *
     * @param Illuminate\Http\Request $request
     * @param Illuminate\Database\Eloquent\Builder $products
     * @return \Illuminate\Database\Eloquent\Builder
     */
    public function filterShoe(Builder $products, Request $request)
    {
        $gender = $request->has('gender') ? $request->gender : false;
        error_log($gender);
        $series = $request->has('series') ? $request->series : false;
        $shape = $request->has('shape') ? $request->shape : false;

        $series ? $products = $products->whereHas('shoe', fn(Builder $query) => $query->where('series', $series)) : '';
        if ($gender === '0' || $gender === '1') {
            $products = $products
                ->whereHas('shoe', fn(Builder $query) => $query->where('gender', $gender)->orWhere('gender', '2'));
        }

        $shape ? $products = $products->whereHas('shoe', fn(Builder $query) => $query->where('shape', $shape)) : '';

        return $products;
    }

    /**
     * Filter the clothes products based on the request and return the filtered products
     *
     * @param Illuminate\Http\Request $request
     * @param Illuminate\Database\Eloquent\Builder $products
     * @return \Illuminate\Database\Eloquent\Builder
     */
    public function filterClothes(Builder $products, Request $request)
    {
        $category = $request->has('category') ? $request->category : false;
        $products = $products
            ->whereHas('clothes', fn(Builder $query) => $category ? $query->where('category', $category) : '');

        return $products;
    }

    /**
     * Filter the accessory products based on the request and return the filtered products
     *
     * @param Illuminate\Http\Request $request
     * @param Illuminate\Database\Eloquent\Builder $products
     * @return \Illuminate\Database\Eloquent\Builder
     */
    public function filterAccessory(Builder $products, Request $request)
    {
        $category = $request->has('category') ? $request->category : false;
        $products = $products
            ->whereHas('accessory', fn(Builder $query) => $category ? $query->where('category', $category) : '');

        return $products;
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function show(Product $product)
    {
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function edit(Product $product)
    {
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Product  $product
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Product $product)
    {
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \Illumniate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function destroy(Request $request)
    {
        if (auth()->user()->role !== 'admin') {
            return response()->json([
                'success' => false,
                'message' => 'You are not authorized to delete this product',
            ], 401);
        }

        $id = $request->product_id;
        $product = Product::find($id);
        if (!$product) {
            return response()->json([
                'success' => false,
                'message' => 'Product not found',
            ], 400);
        }

        $product->delete();

        return response()->json([
            'success' => true,
            'message' => 'Product deleted successfully',
        ]);
    }
}
