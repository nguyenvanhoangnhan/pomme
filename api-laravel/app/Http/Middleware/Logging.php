<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Support\Facades\Log;

class Logging
{
    public function handle($request, Closure $next)
    {
        $client_ip = $request->header('X-Forwarded-For');
        $request_method = $request->method();
        $request_url = $request->url();
        $user_agent = $request->server('HTTP_USER_AGENT');
        $msg = "Request coming {'client-IP': '$client_ip', 'request-method': '$request_method', 'url': '$request_url', 'user-agent': '$user_agent'}";
        Log::build([
            'driver' => 'single',
            'path' => storage_path('logs/app.log'),
        ])->info($msg);

        return $next($request);
    }
}
