<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Shoe extends Model
{
    use HasFactory;
    protected $fillable = [
        'product_id',
        'gender',
        'series',
        'shape',
    ];

    public function product() {
        return $this->belongsTo(Product::class, 'product_id', 'id');
    }
    public function children() {
        return $this->hasMany(ShoeChild::class, 'shoe_id', 'id');
    }
}
