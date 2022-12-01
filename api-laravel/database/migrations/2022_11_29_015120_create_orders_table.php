<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateOrdersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('orders', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('user_id');
            $table->string('address');
            $table->string('province_code');
            $table->string('district_code');
            $table->string('commune_code');
            $table->string('phone');
            $table->string('status')->default('pending');
            $table->unsignedBigInteger('total');
            $table->unsignedBigInteger('discount')->default(0);
            $table->timestamps();
            $table->dateTime('shipping_at')->nullable();
            $table->dateTime('delivered_at')->nullable();
            $table->string('image_url')->nullable()->default('https://via.placeholder.com/500/41B883/ffffff?text=Image');
            $table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('orders');
    }
}
