<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    use HasFactory;

    protected $fillable = [
        'name',
        'price',
        'discount_percent',
        'in_stock',
        'sold',
        'type',
    ];

    public function images()
    {
        return $this->hasMany(Image::class, 'product_id', 'id');
    }

    public function thumbnail()
    {
        return $this->hasOne(Image::class, 'product_id', 'id')->where('is_thumbnail', true);
    }

    public function clothes()
    {
        return $this->hasOne(Clothes::class, 'product_id', 'id');
    }

    public function shoe()
    {
        return $this->hasOne(Shoe::class, 'product_id', 'id');
    }

    public function accessory()
    {
        return $this->hasOne(Accessory::class, 'product_id', 'id');
    }
}
