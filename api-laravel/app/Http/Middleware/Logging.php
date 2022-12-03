<?php


namespace App\Http\Middleware;

use Illuminate\Support\Facades\Log;
use Closure;

class Logging
{
    public function handle($request, Closure $next)
    {
        $msg = join(" ", array($request->header('X-Forwarded-For'), $request->url(), $request->method(), $request->server('HTTP_USER_AGENT'))); 
        Log::build([
            'driver' => 'single',
            'path' => storage_path('logs/app.log'),
        ])->info($msg);

        return $next($request);
    }
}
