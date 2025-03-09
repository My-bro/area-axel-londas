import { headers } from 'next/headers';
import { fetchServices, fetchServiceActions, fetchServiceReactions } from '@/lib/api';
import { Service } from '@/lib/types';

export async function GET(request: Request) {
  const headersList = headers();
  let clientIp = headersList.get('x-forwarded-for') || request.headers.get('x-real-ip') || '127.0.0.1';

  if (clientIp === '::1') {
    clientIp = '127.0.0.1';
  }
  clientIp = clientIp.split(',')[0].trim();

  try {
    const servicesData = await fetchServices();
    const services = Array.isArray(servicesData) ? servicesData : [];
    const processedServices = await Promise.all(services.map(async (service: Service) => {

      try {
        const actionsData = await fetchServiceActions(service.id);
        const reactionsData = await fetchServiceReactions(service.id);
        const actions = Array.isArray(actionsData) ? actionsData : [];
        const reactions = Array.isArray(reactionsData) ? reactionsData : [];

        return {
          name: service.name.toLowerCase(),
          actions: actions.map(action => ({
            name: action.title,
            description: action.description
          })),
          reactions: reactions.map(reaction => ({
            name: reaction.title,
            description: reaction.description
          }))
        };
      } catch (error) {
        console.error(`Error processing service ${service.name}:`, error);
        return null;
      }
    }));

    const filteredServices = processedServices.filter(Boolean);
    const responseData = {
      client: { host: clientIp },
      server: {
        current_time: Math.floor(Date.now() / 1000),
        services: filteredServices
      }
    };

    return new Response(JSON.stringify(responseData, null, 2), {
      headers: { 'content-type': 'application/json' },
    });
  } catch (error) {
    console.error('Fatal error in about.json route:', error);
    return new Response(JSON.stringify({ error: 'Internal Server Error' }), {
      status: 500,
      headers: { 'content-type': 'application/json' },
    });
  }
}

export const dynamic = 'force-dynamic';