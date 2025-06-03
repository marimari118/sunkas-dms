import { resolve } from 'path';
import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
    root: resolve(__dirname, 'src'),
    build: {
        outDir: resolve(__dirname, '../app/flaskr/static'),
        emptyOutDir: false,
        rollupOptions: {
            input: {
                main: resolve(__dirname, 'src/index.ts'),
            },
            output: {
                entryFileNames: 'index.js',
                assetFileNames: 'style.css',
            },
        },
        minify: true,
        cssMinify: true,
    },
    plugins: [
        tailwindcss(),
    ],
});