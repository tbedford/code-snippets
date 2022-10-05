const NodeGeocoder = require('node-geocoder');
 
const options = {
  provider: 'google',
 
  // Optional depending on the providers
  fetch: customFetchImplementation,
  apiKey: 'YOUR_API_KEY', // for Mapquest, OpenCage, Google Premier
  formatter: null // 'gpx', 'string', ...
};
 
const geocoder = NodeGeocoder(options);
 
// Using callback
const res = await geocoder.geocode('29 champs elysée paris');
 
// output :
/*
[
  {
    latitude: 48.8698679,
    longitude: 2.3072976,
    country: 'France',
    countryCode: 'FR',
    city: 'Paris',
    zipcode: '75008',
    streetName: 'Champs-Élysées',
    streetNumber: '29',
    administrativeLevels: {
      level1long: 'Île-de-France',
      level1short: 'IDF',
      level2long: 'Paris',
      level2short: '75'
    },
    provider: 'google'
  }
];
*/


