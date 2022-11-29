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
}
