<?php

namespace App\Http\Controllers\API;

use App\Http\Controllers\Controller;
use App\Models\Order;
use App\Models\Product;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class OrderController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        if (auth()->user()->role === 'admin') {
            $orders = Order::all();

            return response()->json($orders);
        }

        $userId = auth()->user()->id;
        $orders = Order::where('user_id', $userId)->get();

        return response()->json($orders);
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function store(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'receiver_name' => 'required',
            'address' => 'required',
            'province_code' => 'required',
            'district_code' => 'required',
            'commune_code' => 'required',
            'delivery_fee' => 'required|numeric',
            'phone' => 'required',
            'products' => 'required|array|min:1',
        ]);

        if ($validator->fails()) {
            return response()->json([
                'status' => 'error',
                'message' => $validator->errors(),
            ], 422);
        }

        $totalPrice = 0;
        foreach ($request->products as $product) {
            $totalPrice += $product['price_at_order'] * $product['quantity'];
        }

        // orderName is string contain product names, separated by comma
        $orderName = '';
        foreach ($request->products as $product) {
            $productName = Product::find($product['product_id'])->name;
            $orderName .= $productName.', ';
        }

        $user = auth()->user();

        // create order
        $order = Order::create([
            'user_id' => $user->id,
            'receiver_name' => $request->receiver_name,
            'name' => $orderName,
            'address' => $request->address,
            'province_code' => $request->province_code,
            'district_code' => $request->district_code,
            'commune_code' => $request->commune_code,
            'phone' => $request->phone,
            'delivery_fee' => $request->delivery_fee,
            'total_price' => $totalPrice,
        ]);

        // add products to order
        $order->products()->attach($request->products);

        // change order image to the first product thumbnail
        $order->image_url = $order->products->first()->images->first()->url;

        // save order
        $order->save();

        // clear cart
        $user->cartProducts()->detach();

        return response()->json($order);
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Order  $order
     * @return \Illuminate\Http\JsonResponse
     */
    public function show(Request $request)
    {
        $order = Order::with('products.thumbnail')->find($request->id);
        if (!$order) {
            return response()->json([
                'status' => 'error',
                'message' => 'Order not found',
            ], 404);
        }

        if ($order->user_id !== auth()->user()->id && auth()->user()->role !== 'admin') {
            return response()->json([
                'status' => 'error',
                'message' => 'You are not allowed to access this order',
            ], 403);
        }

        return response()->json($order);
    }

    /**
     * Cancel an order.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function cancel(Request $request)
    {
        $id = $request->id;
        $order = Order::find($id);
        if (!$order) {
            return response()->json([
                'status' => 'error',
                'message' => 'Order not found',
            ], 404);
        }

        if ($order->user_id !== auth()->user()->id && auth()->user()->role !== 'admin') {
            return response()->json([
                'status' => 'error',
                'message' => 'You are not allowed to cancel this order',
            ], 403);
        }

        if ($order->status !== 'pending') {
            return response()->json([
                'status' => 'error',
                'message' => 'Can not cancel this order',
            ], 422);
        }

        $order->status = 'canceled';
        $order->save();

        return response()->json($order);
    }

    /**
     * Change status an order.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function changeStatus(Request $request)
    {
        // status must be "pending", "shipping", "delivered", "canceled"
        $validator = Validator::make($request->all(), [
            'status' => 'required|in:pending,shipping,delivered,canceled',
        ]);

        if ($validator->fails()) {
            return response()->json([
                'status' => 'error',
                'message' => $validator->errors(),
            ], 422);
        }

        if (auth()->user()->role !== 'admin') {
            return response()->json([
                'status' => 'error',
                'message' => 'You are not allowed to change order status',
            ], 403);
        }

        $id = $request->id;
        $order = Order::find($id);
        if (!$order) {
            return response()->json([
                'status' => 'error',
                'message' => 'Order not found',
            ], 404);
        }

        $order->status = $request->status;
        if ($request->status === 'shipping') {
            $order->shipping_at = now();
        }

        if ($request->status === 'delivered') {
            $order->delivered_at = now();
        }

        $order->save();

        return response()->json($order);
    }

    /**
     * Put order to finished queue in admin site and add sold to product.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\JsonResponse
     */
    public function finishOrder(Request $request)
    {
        $id = $request->id;
        $order = Order::find($id);
        if (!$order) {
            return response()->json([
                'status' => 'error',
                'message' => 'Order not found',
            ], 404);
        }

        $order->status = 'finished';
        for ($i = 0; $i < count($order->products); $i++) {
            $order->products[$i]->sold += $order->products[$i]->pivot->quantity;
            $order->products[$i]->save();
        }

        $order->save();
    }
}
