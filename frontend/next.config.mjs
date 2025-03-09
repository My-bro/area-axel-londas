/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'api.skead.fr',
        pathname: '/services/**',
      },
    ],
    dangerouslyAllowSVG: true,
  },
};

export default nextConfig;