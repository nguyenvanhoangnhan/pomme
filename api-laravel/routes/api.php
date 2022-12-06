<?php

use App\Http\Controllers\API\AccessoryController;
use App\Http\Controllers\API\AuthController;
use App\Http\Controllers\API\ClothesController;
use App\Http\Controllers\API\OrderController;
use App\Http\Controllers\API\ProductController;
use App\Http\Controllers\API\ShoeController;
use App\Http\Controllers\API\UserController;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::group([
    'middleware' => 'api',
    'prefix' => 'auth',

], function ($router) {
    Route::post('/login', [AuthController::class, 'login']);
    Route::post('/register', [AuthController::class, 'register']);
    Route::post('/logout', [AuthController::class, 'logout']);
    Route::post('/refresh', [AuthController::class, 'refresh']);
    Route::get('/user-profile', [AuthController::class, 'userProfile']);
    Route::post('/change-pass', [AuthController::class, 'changePassWord']);
});

Route::group([
    'middleware' => 'api',
    'prefix' => 'products',

], function ($router) {
    Route::get('/', [ProductController::class, 'index']);
    Route::get('shoes/{product_id}', [ShoeController::class, 'show'])
        ->where('product_id', '[0-9]+');
    Route::get('accessories/{product_id}', [AccessoryController::class, 'show'])
        ->where('product_id', '[0-9]+');
    Route::get('clothes/{product_id}', [ClothesController::class, 'show'])
        ->where('product_id', '[0-9]+');

    // admin only
    Route::post('shoes', [ShoeController::class, 'store']);
    Route::put('shoes', [ShoeController::class, 'update']);
    Route::post('accessories', [AccessoryController::class, 'store']);
    Route::put('accessories', [AccessoryController::class, 'update']);
    Route::post('clothes', [ClothesController::class, 'store']);
    Route::put('clothes', [ClothesController::class, 'update']);
});


Route::group([
    'middleware' => 'api',
    'prefix' => 'orders',

], function ($router) {
    Route::get('/', [OrderController::class, 'index']);
    Route::get('{id}', [OrderController::class, 'show']);
    Route::post('/', [OrderController::class, 'store']);
    Route::post('cancel/{id}', [OrderController::class, 'cancel'])
        ->where('id', '[0-9]+');

    Route::put('{id}/status', [OrderController::class, 'changeStatus'])
        ->where('id', '[0-9]+');
});


Route::group([
    'middleware' => 'api',
    'prefix' => 'users',
], function ($router) {
});


Route::group([
    'middleware' => 'api',
    'prefix' => 'cart',
], function ($router) {
    Route::get('/', [UserController::class, 'cartProducts']);
    Route::post('/', [UserController::class, 'addToCart']);
    Route::post('{product_id}', [UserController::class, 'updateCartPivot'])
        ->where('product_id', '[0-9]+');
    Route::delete('/', [UserController::class, 'clearCart']);
    Route::delete('{cart_product_id}', [UserController::class, 'removeFromCart'])
        ->where('id', '[0-9]+');
});


Route::group([
    'middleware' => 'api',
    'prefix' => 'love',
], function ($router) {
    Route::get('/', [UserController::class, 'loveProducts']);
    Route::post('{product_id}', [UserController::class, 'toggleLoveProduct'])
        ->where('product_id', '[0-9]+');
});
