<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ShoeChild extends Model
{
    use HasFactory;
    protected $fillable = [
        'shoe_id',
        'size',
        'in_stock',
    ];
}
