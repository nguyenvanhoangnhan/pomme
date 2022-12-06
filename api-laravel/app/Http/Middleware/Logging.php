<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Support\Facades\Log;

class Logging
{
    public function handle($request, Closure $next)
    {
        $clientIp = $request->header('X-Forwarded-For');
        $requestMethod = $request->method();
        $requestUrl = $request->url();
        $userAgent = $request->server('HTTP_USER_AGENT');
        $msg = "Request coming {\"client-IP\": \"$clientIp\", \"request-method\": \"$requestMethod\", \"url\": \"$requestUrl\", \"user-agent\": \"$userAgent\"}";
        Log::build([
            'driver' => 'single',
            'path' => storage_path('logs/app.log'),
        ])->info($msg);

        return $next($request);
    }
}
