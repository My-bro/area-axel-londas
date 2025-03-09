import { promises as fs } from 'fs';
import { join } from 'path';

export const dynamic = 'force-dynamic';

export async function GET() {
  const localPath = join(process.cwd(), 'public', 'app-release.apk');

  try {
    try {
      await fs.access(localPath);
    } catch {
      throw new Error(`File not accessible at ${localPath}`);
    }

    const stats = await fs.stat(localPath);

    if (stats.size === 0) {
      throw new Error('Local APK file is empty');
    }

    const fileBuffer = await fs.readFile(localPath);

    return new Response(fileBuffer, {
      status: 200,
      headers: {
        'Content-Type': 'application/vnd.android.package-archive',
        'Content-Length': stats.size.toString(),
        'Content-Disposition': 'attachment; filename="app-release.apk"',
        'Cache-Control': 'no-store, no-cache, must-revalidate, private',
        'Pragma': 'no-cache',
        'X-Source': 'local-file',
        'Expires': '0'
      }
    });
  } catch {
    return new Response(null, {
      status: 302,
      headers: {
        'Location': 'https://github.com/julesreyn/area/releases/download/latest/app-release.apk',
        'Cache-Control': 'no-store, no-cache, must-revalidate, private',
        'Pragma': 'no-cache',
        'X-Source': 'github-redirect',
        'Expires': '0'
      }
    });
  }
}
