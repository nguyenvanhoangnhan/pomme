<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Order extends Model
{
    use HasFactory;
    protected $fillable = [
        'user_id',
        'name',
        'receiver_name',
        'address',
        'province_code',
        'district_code',
        'commune_code',
        'phone',
        'status',
        'total_price',
        'delivery_fee',
        'discount',
        'shipping_at',
        'delivered_at',
        'image_url',
    ];

    public function products()
    {
        // order-products table is pivot table of order and product
        return $this->belongsToMany(Product::class, 'order_products', 'order_id', 'product_id')
            ->withPivot('price_at_order', 'quantity', 'size')
            ->withTimestamps();
    }
}
