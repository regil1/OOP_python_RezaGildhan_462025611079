<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">

        <title>{{ config('app.name', 'FiskalCode') }}</title>
        <link rel="icon" type="image/x-icon" href="{{ asset('favicon.ico') }}">

        <!-- Fonts -->
        <link rel="preconnect" href="https://fonts.bunny.net">
        <link href="https://fonts.bunny.net/css?family=figtree:400,500,600&display=swap" rel="stylesheet" />

        <!-- ========================================== -->
        <!-- SOLUSI: GANTI VITE DENGAN CDN (PASTI JALAN) -->
        <!-- ========================================== -->

        <!-- 1. Tailwind CSS (Agar tampilan langsung rapi) -->
        <script src="https://cdn.tailwindcss.com"></script>

        <!-- 2. Chart.js (Agar grafik di dashboard muncul) -->
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

        <!-- 3. Konfigurasi Tailwind (Untuk Dark Mode & Warna) -->
        <script>
            tailwind.config = {
                darkMode: 'class',
                theme: {
                    extend: {
                        colors: {
                            primary: '#4F46E5',
                            secondary: '#10B981',
                        }
                    }
                }
            }
        </script>
    </head>
    <body class="font-sans antialiased">
        <div class="min-h-screen bg-gray-100 dark:bg-gray-900">
            @include('layouts.navigation')

            <!-- Page Heading -->
            @isset($header)
                <header class="bg-white dark:bg-gray-800 shadow">
                    <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                        {{ $header }}
                    </div>
                </header>
            @endisset

            <!-- Page Content -->
            <main>
                {{ $slot }}
            </main>
        </div>
    </body>
</html>
