import sys
import json
import re

states = {
  "ak" : {
    "keywords" : [ "alaska" ],
    "statelongname" : "alaska"
  },
  "al" : {
    "borders" : [ { "lat" : 34.957996, "lng" : -88.154297 },
      { "lat" : 34.994003, "lng" : -85.649414 },
      { "lat" : 32.324276, "lng" : -84.946289 },
      { "lat" : 31.653381, "lng" : -85.078125 },
      { "lat" : 31.01528, "lng" : -84.946289 },
      { "lat" : 30.939924, "lng" : -87.583008 },
      { "lat" : 30.448673, "lng" : -87.495117 },
      { "lat" : 30.448673, "lng" : -88.505859 },
      { "lat" : 34.957996, "lng" : -88.154297 } ],
    "keywords" : [ "alabama" ],
    "statelongname" : "Alabama"
  },
  "ar" : {
    "borders" : [ { "lat" : 36.597889, "lng" : -94.570312 },
      { "lat" : 36.562599, "lng" : -90.175781 },
      { "lat" : 35.853439, "lng" : -90.395508 },
      { "lat" : 36.03133, "lng" : -89.648438 },
      { "lat" : 33.797409, "lng" : -91.142578 },
      { "lat" : 33.284618, "lng" : -91.230469 },
      { "lat" : 33.100746, "lng" : -93.911133 },
      { "lat" : 33.61462, "lng" : -94.042969 },
      { "lat" : 33.724339, "lng" : -94.526367 },
      { "lat" : 35.924644, "lng" : -94.526367 },
      { "lat" : 36.597889, "lng" : -94.570312 } ],
    "keywords" : [ "arkansas" ],
    "statelongname" : "Arkansas"
  },
  "as" : {
    "keywords" : [ "american samoa", "samoa" ],
    "statelongname" : "American samoa"
  },
  "az" : {
    "borders" : [ { "lat" : 32.546814, "lng" : -115.092773 },
      { "lat" : 31.278551, "lng" : -110.961914 },
      { "lat" : 31.316101, "lng" : -109.072266 },
      { "lat" : 37.055176, "lng" : -109.379883 },
      { "lat" : 37.0201, "lng" : -111.181641 },
      { "lat" : 36.244274, "lng" : -112.060547 },
      { "lat" : 35.995785, "lng" : -114.609375 },
      { "lat" : 34.379711, "lng" : -114.389648 },
      { "lat" : 32.546814, "lng" : -115.092773 } ],
    "keywords" : [ "arizona", "phoenix" ],
    "statelongname" : "Arizona"
  },
  "ca" : {
    "borders" : [ { "lat" : 32.620869, "lng" : -117.246094 },
      { "lat" : 32.768799, "lng" : -114.873047 },
      { "lat" : 34.452217, "lng" : -114.433594 },
      { "lat" : 39.027718, "lng" : -119.794922 },
      { "lat" : 41.967659, "lng" : -119.970703 },
      { "lat" : 42.032974, "lng" : -124.365234 },
      { "lat" : 39.639538, "lng" : -123.837891 },
      { "lat" : 35.029995, "lng" : -120.673828 },
      { "lat" : 33.651207, "lng" : -117.773438 },
      { "lat" : 32.620869, "lng" : -117.246094 } ],
    "keywords" : [ "california", "hollywood", "san francisco", "los angeles", "san diego" ],
    "statelongname" : "California"
  },
  "co" : {
    "borders" : [ { "lat" : 40.913513, "lng" : -102.172852 },
      { "lat" : 36.985004, "lng" : -102.084961 },
      { "lat" : 37.055176, "lng" : -109.116211 },
      { "lat" : 41.046219, "lng" : -109.116211 },
      { "lat" : 40.913513, "lng" : -102.172852 } ],
    "keywords" : [ "colorado" ],
    "statelongname" : "Colorado"
  },
  "ct" : {
    "borders" : [ { "lat" : 42.016651, "lng" : -71.806641 },
      { "lat" : 41.335575, "lng" : -71.828613 },
      { "lat" : 41.26955, "lng" : -72.971191 },
      { "lat" : 40.996483, "lng" : -73.652344 },
      { "lat" : 42.065605, "lng" : -73.45459 },
      { "lat" : 42.016651, "lng" : -71.806641 } ],
    "keywords" : [ "connecticut" ],
    "statelongname" : "Connecticut"
  },
  "dc" : {
    "keywords" : [ "district of columbia" ],
    "statelongname" : "District of Columbia"
  },
  "de" : {
    "borders" : [ { "lat" : 38.82259, "lng" : -75.135498 },
      { "lat" : 39.436192, "lng" : -75.476074 },
      { "lat" : 39.876019, "lng" : -75.498047 },
      { "lat" : 39.67337, "lng" : -75.9375 },
      { "lat" : 38.513786, "lng" : -75.717773 },
      { "lat" : 38.462193, "lng" : -75.025635 },
      { "lat" : 38.82259, "lng" : -75.135498 } ],
    "keywords" : [ "delaware" ],
    "statelongname" : "Delaware"
  },
  "fl" : {
    "borders" : [ { "lat" : 30.259068, "lng" : -87.539062 },
      { "lat" : 30.97761, "lng" : -87.583008 },
      { "lat" : 31.052935, "lng" : -85.03418 },
      { "lat" : 30.600094, "lng" : -81.474609 },
      { "lat" : 29.535231, "lng" : -81.298828 },
      { "lat" : 26.824072, "lng" : -80.024414 },
      { "lat" : 25.125393, "lng" : -80.507812 },
      { "lat" : 26.115986, "lng" : -81.782227 },
      { "lat" : 27.605671, "lng" : -82.749023 },
      { "lat" : 28.806173, "lng" : -82.617188 },
      { "lat" : 30.145126, "lng" : -83.891602 },
      { "lat" : 30.031055, "lng" : -84.550781 },
      { "lat" : 29.688053, "lng" : -85.209961 },
      { "lat" : 30.334953, "lng" : -86.264648 },
      { "lat" : 30.259068, "lng" : -87.539062 } ],
    "keywords" : [ "florida", "tampa", "miami", "callahan" ],
    "statelongname" : "Florida"
  },
  "ga" : {
    "borders" : [ { "lat" : 34.957996, "lng" : -85.693359 },
      { "lat" : 32.287132, "lng" : -84.946289 },
      { "lat" : 31.690783, "lng" : -85.166016 },
      { "lat" : 31.01528, "lng" : -85.03418 },
      { "lat" : 30.713505, "lng" : -81.606445 },
      { "lat" : 32.175613, "lng" : -80.859375 },
      { "lat" : 33.284618, "lng" : -81.826172 },
      { "lat" : 34.597042, "lng" : -83.144531 },
      { "lat" : 35.101933, "lng" : -83.276367 },
      { "lat" : 34.957996, "lng" : -85.693359 } ],
    "keywords" : [ "georgia", "atlanta" ],
    "statelongname" : "Georgia"
  },
  "gu" : {
    "keywords" : [ "guam" ],
    "statelongname" : "Guam"
  },
  "hi" : {
    "keywords" : [ "hawaii" ],
    "statelongname" : "Hawaii"
  },
  "ia" : {
    "borders" : [ { "lat" : 43.484814, "lng" : -96.416016 },
      { "lat" : 42.455887, "lng" : -96.416016 },
      { "lat" : 40.613953, "lng" : -95.537109 },
      { "lat" : 40.613953, "lng" : -91.40625 },
      { "lat" : 41.211723, "lng" : -90.966797 },
      { "lat" : 41.57436, "lng" : -91.098633 },
      { "lat" : 41.804077, "lng" : -90.175781 },
      { "lat" : 42.195969, "lng" : -90.219727 },
      { "lat" : 42.747013, "lng" : -91.010742 },
      { "lat" : 43.516689, "lng" : -91.318359 },
      { "lat" : 43.484814, "lng" : -96.416016 } ],
    "keywords" : [ "iowa" ],
    "statelongname" : "Iowa"
  },
  "id" : {
    "borders" : [ { "lat" : 42.163403, "lng" : -116.982422 },
      { "lat" : 42.098221, "lng" : -111.005859 },
      { "lat" : 44.653023, "lng" : -111.269531 },
      { "lat" : 44.402393, "lng" : -112.939453 },
      { "lat" : 45.521744, "lng" : -114.082031 },
      { "lat" : 45.460133, "lng" : -114.697266 },
      { "lat" : 46.619263, "lng" : -114.433594 },
      { "lat" : 47.989922, "lng" : -116.191406 },
      { "lat" : 49.037868, "lng" : -116.103516 },
      { "lat" : 48.922501, "lng" : -117.158203 },
      { "lat" : 42.163403, "lng" : -116.982422 } ],
    "keywords" : [ "idaho" ],
    "statelongname" : "Idaho"
  },
  "il" : {
    "borders" : [ { "lat" : 37.0201, "lng" : -89.208984 },
      { "lat" : 38.925228, "lng" : -90.175781 },
      { "lat" : 39.842285, "lng" : -91.538086 },
      { "lat" : 40.580585, "lng" : -91.40625 },
      { "lat" : 41.112469, "lng" : -90.966797 },
      { "lat" : 41.508575, "lng" : -91.142578 },
      { "lat" : 41.771313, "lng" : -90.219727 },
      { "lat" : 42.130821, "lng" : -90.131836 },
      { "lat" : 42.455887, "lng" : -90.615234 },
      { "lat" : 42.553082, "lng" : -87.890625 },
      { "lat" : 41.70573, "lng" : -87.451172 },
      { "lat" : 39.130058, "lng" : -87.670898 },
      { "lat" : 38.719807, "lng" : -87.495117 },
      { "lat" : 38.065392, "lng" : -88.022461 },
      { "lat" : 37.09024, "lng" : -88.505859 },
      { "lat" : 37.0201, "lng" : -89.208984 } ],
    "keywords" : [ "illinois", "chicago" ],
    "statelongname" : "Illinois"
  },
  "in" : {
    "borders" : [ { "lat" : 39.164143, "lng" : -84.814453 },
      { "lat" : 41.738529, "lng" : -84.858398 },
      { "lat" : 41.804077, "lng" : -86.572266 },
      { "lat" : 41.541477, "lng" : -87.583008 },
      { "lat" : 39.232254, "lng" : -87.714844 },
      { "lat" : 38.719807, "lng" : -87.495117 },
      { "lat" : 37.961521, "lng" : -88.198242 },
      { "lat" : 37.857506, "lng" : -87.011719 },
      { "lat" : 38.238178, "lng" : -85.957031 },
      { "lat" : 39.164143, "lng" : -84.814453 } ],
    "keywords" : [ "indiana" ],
    "statelongname" : "Indiana"
  },
  "ks" : {
    "borders" : [ { "lat" : 40.010788, "lng" : -102.041016 },
      { "lat" : 40.010788, "lng" : -94.921875 },
      { "lat" : 39.402245, "lng" : -95.009766 },
      { "lat" : 38.82259, "lng" : -94.526367 },
      { "lat" : 36.985004, "lng" : -94.746094 },
      { "lat" : 37.09024, "lng" : -102.084961 },
      { "lat" : 40.010788, "lng" : -102.041016 } ],
    "keywords" : [ "kansas" ],
    "statelongname" : "Kansas"
  },
  "ky" : {
    "borders" : [ { "lat" : 37.544579, "lng" : -82.045898 },
      { "lat" : 38.134556, "lng" : -82.661133 },
      { "lat" : 38.616871, "lng" : -82.661133 },
      { "lat" : 38.719807, "lng" : -83.452148 },
      { "lat" : 38.82259, "lng" : -84.418945 },
      { "lat" : 39.164143, "lng" : -84.902344 },
      { "lat" : 38.134556, "lng" : -85.869141 },
      { "lat" : 37.857506, "lng" : -87.1875 },
      { "lat" : 37.857506, "lng" : -88.198242 },
      { "lat" : 37.055176, "lng" : -88.505859 },
      { "lat" : 37.09024, "lng" : -89.165039 },
      { "lat" : 36.527294, "lng" : -89.033203 },
      { "lat" : 36.527294, "lng" : -83.803711 },
      { "lat" : 37.544579, "lng" : -82.045898 } ],
    "keywords" : [ "kentucky", "campbellsville" ],
    "statelongname" : "Kentucky"
  },
  "la" : {
    "borders" : [ { "lat" : 33.13755, "lng" : -93.867188 },
      { "lat" : 33.284618, "lng" : -91.230469 },
      { "lat" : 32.101189, "lng" : -90.878906 },
      { "lat" : 30.751278, "lng" : -91.757812 },
      { "lat" : 31.128199, "lng" : -89.648438 },
      { "lat" : 29.152161, "lng" : -89.033203 },
      { "lat" : 29.382175, "lng" : -91.757812 },
      { "lat" : 29.993002, "lng" : -93.779297 },
      { "lat" : 33.13755, "lng" : -93.867188 } ],
    "keywords" : [ "louisiana" ],
    "statelongname" : "Louisiana"
  },
  "ma" : {
    "borders" : [ { "lat" : 42.795403, "lng" : -73.344727 },
      { "lat" : 42.730873, "lng" : -72.575684 },
      { "lat" : 42.674358, "lng" : -71.257324 },
      { "lat" : 42.827641, "lng" : -71.05957 },
      { "lat" : 43.020714, "lng" : -70.883789 },
      { "lat" : 42.64204, "lng" : -70.675049 },
      { "lat" : 42.358543, "lng" : -71.015625 },
      { "lat" : 42.261047, "lng" : -70.784912 },
      { "lat" : 41.934978, "lng" : -70.543213 },
      { "lat" : 41.828644, "lng" : -69.938965 },
      { "lat" : 41.672913, "lng" : -69.960938 },
      { "lat" : 41.401535, "lng" : -70.268555 },
      { "lat" : 41.335575, "lng" : -70.751953 },
      { "lat" : 41.590797, "lng" : -71.015625 },
      { "lat" : 42.049294, "lng" : -71.499023 },
      { "lat" : 42.057449, "lng" : -73.432617 },
      { "lat" : 42.795403, "lng" : -73.344727 } ],
    "keywords" : [ "massachusetts", "boston" ],
    "statelongname" : "Massachusetts"
  },
  "md" : {
    "borders" : [ { "lat" : 38.479397, "lng" : -75.146484 },
      { "lat" : 38.548164, "lng" : -75.761719 },
      { "lat" : 39.67337, "lng" : -75.849609 },
      { "lat" : 39.774769, "lng" : -77.958984 },
      { "lat" : 39.478607, "lng" : -78.299561 },
      { "lat" : 39.172661, "lng" : -77.88208 },
      { "lat" : 39.334297, "lng" : -77.67334 },
      { "lat" : 38.82259, "lng" : -76.948242 },
      { "lat" : 38.341656, "lng" : -77.387695 },
      { "lat" : 37.892197, "lng" : -76.113281 },
      { "lat" : 36.809284, "lng" : -76.113281 },
      { "lat" : 38.479397, "lng" : -75.146484 } ],
    "keywords" : [ "maryland" ],
    "statelongname" : "Maryland"
  },
  "me" : {
    "borders" : [ { "lat" : 44.855869, "lng" : -66.862793 },
      { "lat" : 45.213005, "lng" : -67.214355 },
      { "lat" : 45.166546, "lng" : -67.456055 },
      { "lat" : 45.598667, "lng" : -67.5 },
      { "lat" : 45.752193, "lng" : -67.851562 },
      { "lat" : 47.129951, "lng" : -67.807617 },
      { "lat" : 47.457809, "lng" : -68.334961 },
      { "lat" : 47.204643, "lng" : -68.90625 },
      { "lat" : 47.457809, "lng" : -69.191895 },
      { "lat" : 46.739861, "lng" : -70.026855 },
      { "lat" : 46.422714, "lng" : -70.158691 },
      { "lat" : 46.149395, "lng" : -70.334473 },
      { "lat" : 45.58329, "lng" : -70.686035 },
      { "lat" : 45.259422, "lng" : -71.081543 },
      { "lat" : 42.988575, "lng" : -70.839844 },
      { "lat" : 44.119141, "lng" : -69.016113 },
      { "lat" : 44.386692, "lng" : -68.115234 },
      { "lat" : 44.855869, "lng" : -66.862793 } ],
    "keywords" : [ "maine" ],
    "statelongname" : "Maine"
  },
  "mi" : {
    "borders" : [ { "lat" : 41.804077, "lng" : -86.660156 },
      { "lat" : 42.455887, "lng" : -86.176758 },
      { "lat" : 43.675819, "lng" : -86.484375 },
      { "lat" : 44.84029, "lng" : -86.132812 },
      { "lat" : 45.8288, "lng" : -85.03418 },
      { "lat" : 45.182037, "lng" : -83.320312 },
      { "lat" : 44.370987, "lng" : -83.452148 },
      { "lat" : 43.92955, "lng" : -83.891602 },
      { "lat" : 44.150681, "lng" : -82.96875 },
      { "lat" : 42.908161, "lng" : -82.265625 },
      { "lat" : 42.326061, "lng" : -83.276367 },
      { "lat" : 41.934978, "lng" : -83.276367 },
      { "lat" : 41.738529, "lng" : -83.979492 },
      { "lat" : 41.804077, "lng" : -86.660156 } ],
    "keywords" : [ "michigan", "detroit" ],
    "statelongname" : "Michigan"
  },
  "mn" : {
    "borders" : [ { "lat" : 43.452919, "lng" : -96.416016 },
      { "lat" : 43.516689, "lng" : -91.318359 },
      { "lat" : 43.961189, "lng" : -91.230469 },
      { "lat" : 44.902576, "lng" : -92.900391 },
      { "lat" : 45.644768, "lng" : -92.900391 },
      { "lat" : 46.437859, "lng" : -92.109375 },
      { "lat" : 47.931065, "lng" : -92.373047 },
      { "lat" : 49.037868, "lng" : -95.185547 },
      { "lat" : 49.037868, "lng" : -97.294922 },
      { "lat" : 47.04018, "lng" : -96.328125 },
      { "lat" : 43.452919, "lng" : -96.416016 } ],
    "keywords" : [ "minnesota" ],
    "statelongname" : "Minnesota"
  },
  "mo" : {
    "borders" : [ { "lat" : 40.613953, "lng" : -91.450195 },
      { "lat" : 39.808537, "lng" : -91.494141 },
      { "lat" : 38.719807, "lng" : -90.219727 },
      { "lat" : 36.633163, "lng" : -89.033203 },
      { "lat" : 36.03133, "lng" : -89.736328 },
      { "lat" : 35.924644, "lng" : -90.483398 },
      { "lat" : 36.703659, "lng" : -90.131836 },
      { "lat" : 36.597889, "lng" : -94.790039 },
      { "lat" : 39.027718, "lng" : -94.482422 },
      { "lat" : 39.436192, "lng" : -94.921875 },
      { "lat" : 39.977119, "lng" : -94.833984 },
      { "lat" : 40.111691, "lng" : -95.405273 },
      { "lat" : 40.647305, "lng" : -95.493164 },
      { "lat" : 40.613953, "lng" : -91.450195 } ],
    "keywords" : [ "missouri" ],
    "statelongname" : "Missouri"
  },
  "mp" : {
    "keywords" : [ "northern mariana islands" ],
    "statelongname" : "Northern Mariana Islands"
  },
  "ms" : {
    "borders" : [ { "lat" : 34.92197, "lng" : -88.110352 },
      { "lat" : 30.334953, "lng" : -88.461914 },
      { "lat" : 30.221102, "lng" : -89.516602 },
      { "lat" : 31.203405, "lng" : -89.736328 },
      { "lat" : 31.01528, "lng" : -91.538086 },
      { "lat" : 31.690783, "lng" : -91.538086 },
      { "lat" : 32.212803, "lng" : -91.010742 },
      { "lat" : 33.760883, "lng" : -91.186523 },
      { "lat" : 34.957996, "lng" : -90.175781 },
      { "lat" : 34.92197, "lng" : -88.110352 } ],
    "keywords" : [ "mississippi" ],
    "statelongname" : "Mississippi"
  },
  "mt" : {
    "borders" : [ { "lat" : 48.980217, "lng" : -104.0625 },
      { "lat" : 45.089035, "lng" : -104.0625 },
      { "lat" : 45.151054, "lng" : -111.181641 },
      { "lat" : 44.527843, "lng" : -111.09375 },
      { "lat" : 44.402393, "lng" : -113.027344 },
      { "lat" : 45.58329, "lng" : -114.082031 },
      { "lat" : 45.3367, "lng" : -114.873047 },
      { "lat" : 46.739861, "lng" : -114.433594 },
      { "lat" : 47.219566, "lng" : -116.103516 },
      { "lat" : 49.037868, "lng" : -116.015625 },
      { "lat" : 48.980217, "lng" : -104.0625 } ],
    "keywords" : [ "montana" ],
    "statelongname" : "Montana"
  },
  "na" : {
    "keywords" : [ "national" ],
    "statelongname" : "National"
  },
  "nc" : {
    "borders" : [ { "lat" : 36.633163, "lng" : -75.893555 },
      { "lat" : 36.562599, "lng" : -81.606445 },
      { "lat" : 36.102375, "lng" : -82.265625 },
      { "lat" : 35.532227, "lng" : -83.496094 },
      { "lat" : 35.101933, "lng" : -84.375 },
      { "lat" : 34.994003, "lng" : -83.100586 },
      { "lat" : 35.317368, "lng" : -82.397461 },
      { "lat" : 34.849876, "lng" : -79.49707 },
      { "lat" : 33.760883, "lng" : -78.530273 },
      { "lat" : 34.849876, "lng" : -76.948242 },
      { "lat" : 35.532227, "lng" : -75.805664 },
      { "lat" : 36.633163, "lng" : -75.893555 } ],
    "keywords" : [ "north carolina" ],
    "statelongname" : "North Carolina"
  },
  "nd" : {
    "borders" : [ { "lat" : 48.922501, "lng" : -97.207031 },
      { "lat" : 45.8288, "lng" : -96.591797 },
      { "lat" : 46.012222, "lng" : -104.150391 },
      { "lat" : 49.095451, "lng" : -104.0625 },
      { "lat" : 48.922501, "lng" : -97.207031 } ],
    "keywords" : [ "north dakota" ],
    "statelongname" : "North Dakota"
  },
  "ne" : {
    "borders" : [ { "lat" : 43.06889, "lng" : -104.106445 },
      { "lat" : 43.036777, "lng" : -98.4375 },
      { "lat" : 42.553082, "lng" : -96.416016 },
      { "lat" : 39.943436, "lng" : -95.273438 },
      { "lat" : 40.178871, "lng" : -102.172852 },
      { "lat" : 40.979897, "lng" : -102.084961 },
      { "lat" : 41.013065, "lng" : -104.150391 },
      { "lat" : 43.06889, "lng" : -104.106445 } ],
    "keywords" : [ "nebraska" ],
    "statelongname" : "Nebraska"
  },
  "nh" : {
    "borders" : [ { "lat" : 42.940338, "lng" : -70.817871 },
      { "lat" : 43.35714, "lng" : -70.905762 },
      { "lat" : 45.274887, "lng" : -71.191406 },
      { "lat" : 45.274887, "lng" : -71.411133 },
      { "lat" : 44.731125, "lng" : -71.674805 },
      { "lat" : 44.418087, "lng" : -71.652832 },
      { "lat" : 44.245197, "lng" : -72.092285 },
      { "lat" : 43.50872, "lng" : -72.421875 },
      { "lat" : 42.755081, "lng" : -72.608643 },
      { "lat" : 42.650124, "lng" : -71.323242 },
      { "lat" : 42.940338, "lng" : -70.817871 } ],
    "keywords" : [ "new hampshire" ],
    "statelongname" : "New Hampshire"
  },
  "nj" : {
    "borders" : [ { "lat" : 40.513798, "lng" : -74.311523 },
      { "lat" : 41.062786, "lng" : -73.959961 },
      { "lat" : 41.376808, "lng" : -74.772949 },
      { "lat" : 40.613953, "lng" : -75.234375 },
      { "lat" : 40.19566, "lng" : -74.816895 },
      { "lat" : 39.825413, "lng" : -75.498047 },
      { "lat" : 39.487083, "lng" : -75.541992 },
      { "lat" : 38.993572, "lng" : -74.86084 },
      { "lat" : 39.520992, "lng" : -74.311523 },
      { "lat" : 40.245991, "lng" : -73.959961 },
      { "lat" : 40.513798, "lng" : -74.311523 } ],
    "keywords" : [ "new jersey" ],
    "statelongname" : "New Jersey"
  },
  "nm" : {
    "borders" : [ { "lat" : 31.353638, "lng" : -108.94043 },
      { "lat" : 31.353638, "lng" : -108.105469 },
      { "lat" : 31.840233, "lng" : -108.149414 },
      { "lat" : 31.989443, "lng" : -106.567383 },
      { "lat" : 32.212803, "lng" : -102.919922 },
      { "lat" : 36.985004, "lng" : -103.007812 },
      { "lat" : 37.0201, "lng" : -109.116211 },
      { "lat" : 31.353638, "lng" : -108.94043 } ],
    "keywords" : [ "new mexico" ],
    "statelongname" : "New Mexico"
  },
  "nv" : {
    "borders" : [ { "lat" : 34.307144, "lng" : -114.433594 },
      { "lat" : 35.960224, "lng" : -114.697266 },
      { "lat" : 36.315125, "lng" : -111.972656 },
      { "lat" : 37.0201, "lng" : -111.09375 },
      { "lat" : 37.09024, "lng" : -113.994141 },
      { "lat" : 41.902279, "lng" : -114.169922 },
      { "lat" : 41.967659, "lng" : -119.794922 },
      { "lat" : 39.027718, "lng" : -119.794922 },
      { "lat" : 34.307144, "lng" : -114.433594 } ],
    "keywords" : [ "nevada" ],
    "statelongname" : "Nevada"
  },
  "ny" : {
    "borders" : [ { "lat" : 44.980343, "lng" : -73.322754 },
      { "lat" : 45.058002, "lng" : -74.772949 },
      { "lat" : 44.182205, "lng" : -76.333008 },
      { "lat" : 43.500751, "lng" : -76.223145 },
      { "lat" : 43.229195, "lng" : -77.453613 },
      { "lat" : 43.389084, "lng" : -78.046875 },
      { "lat" : 43.261208, "lng" : -79.189453 },
      { "lat" : 42.811523, "lng" : -78.815918 },
      { "lat" : 42.163403, "lng" : -79.760742 },
      { "lat" : 41.951321, "lng" : -79.541016 },
      { "lat" : 42.081917, "lng" : -75.344238 },
      { "lat" : 41.376808, "lng" : -74.816895 },
      { "lat" : 41.062786, "lng" : -73.937988 },
      { "lat" : 40.497093, "lng" : -74.289551 },
      { "lat" : 40.563896, "lng" : -73.575439 },
      { "lat" : 40.996483, "lng" : -71.784668 },
      { "lat" : 41.178654, "lng" : -72.290039 },
      { "lat" : 41.004776, "lng" : -72.674561 },
      { "lat" : 40.85537, "lng" : -73.718262 },
      { "lat" : 40.996483, "lng" : -73.652344 },
      { "lat" : 42.666283, "lng" : -73.322754 },
      { "lat" : 43.644028, "lng" : -73.300781 },
      { "lat" : 44.087585, "lng" : -73.45459 },
      { "lat" : 44.980343, "lng" : -73.322754 } ],
    "keywords" : [ "new york", "brooklyn" ],
    "statelongname" : "New York"
  },
  "oh" : {
    "borders" : [ { "lat" : 38.376114, "lng" : -82.661133 },
      { "lat" : 38.582527, "lng" : -82.22168 },
      { "lat" : 39.00211, "lng" : -82.056885 },
      { "lat" : 39.740986, "lng" : -80.859375 },
      { "lat" : 40.363289, "lng" : -80.595703 },
      { "lat" : 42.098221, "lng" : -80.507812 },
      { "lat" : 41.475658, "lng" : -82.30957 },
      { "lat" : 41.804077, "lng" : -83.891602 },
      { "lat" : 41.70573, "lng" : -85.03418 },
      { "lat" : 39.027718, "lng" : -84.726562 },
      { "lat" : 38.376114, "lng" : -82.661133 } ],
    "keywords" : [ "ohio" ],
    "statelongname" : "Ohio"
  },
  "ok" : {
    "borders" : [ { "lat" : 33.651207, "lng" : -94.526367 },
      { "lat" : 35.532227, "lng" : -94.482422 },
      { "lat" : 36.914764, "lng" : -94.790039 },
      { "lat" : 37.055176, "lng" : -102.919922 },
      { "lat" : 36.244274, "lng" : -102.963867 },
      { "lat" : 36.491974, "lng" : -100.063477 },
      { "lat" : 34.488449, "lng" : -100.107422 },
      { "lat" : 33.687782, "lng" : -96.635742 },
      { "lat" : 33.651207, "lng" : -94.526367 } ],
    "keywords" : [ "oklahoma" ],
    "statelongname" : "Oklahoma"
  },
  "or" : {
    "borders" : [ { "lat" : 42.032974, "lng" : -124.277344 },
      { "lat" : 42.098221, "lng" : -116.982422 },
      { "lat" : 46.073231, "lng" : -116.982422 },
      { "lat" : 45.706181, "lng" : -123.837891 },
      { "lat" : 42.032974, "lng" : -124.277344 } ],
    "keywords" : [ "oregon", "portland" ],
    "statelongname" : "Oregon"
  },
  "pa" : {
    "borders" : [ { "lat" : 42.326061, "lng" : -79.936523 },
      { "lat" : 41.967659, "lng" : -79.628906 },
      { "lat" : 42.130821, "lng" : -75.366211 },
      { "lat" : 41.409775, "lng" : -74.750977 },
      { "lat" : 40.580585, "lng" : -75.234375 },
      { "lat" : 40.111691, "lng" : -74.750977 },
      { "lat" : 39.67337, "lng" : -75.893555 },
      { "lat" : 39.757881, "lng" : -80.562744 },
      { "lat" : 42.000324, "lng" : -80.507812 },
      { "lat" : 42.326061, "lng" : -79.936523 } ],
    "keywords" : [ "pennsylvania", "philadelphia" ],
    "statelongname" : "Pennsylvania"
  },
  "pr" : {
    "keywords" : [ "puerto rico" ],
    "statelongname" : "Puerto Rico"
  },
  "ri" : {
    "borders" : [ { "lat" : 41.327328, "lng" : -71.817627 },
      { "lat" : 41.450962, "lng" : -71.05957 },
      { "lat" : 41.70573, "lng" : -71.147461 },
      { "lat" : 42.041134, "lng" : -71.466064 },
      { "lat" : 42.016651, "lng" : -71.806641 },
      { "lat" : 41.664703, "lng" : -71.784668 },
      { "lat" : 41.327328, "lng" : -71.817627 } ],
    "keywords" : [ "rhode island" ],
    "statelongname" : "Rhode Island"
  },
  "sc" : {
    "borders" : [ { "lat" : 33.870415, "lng" : -78.574219 },
      { "lat" : 34.813805, "lng" : -79.672852 },
      { "lat" : 35.029995, "lng" : -81.035156 },
      { "lat" : 35.281502, "lng" : -82.529297 },
      { "lat" : 34.885929, "lng" : -83.276367 },
      { "lat" : 32.249973, "lng" : -80.81543 },
      { "lat" : 33.027088, "lng" : -79.40918 },
      { "lat" : 33.468109, "lng" : -79.057617 },
      { "lat" : 33.870415, "lng" : -78.574219 } ],
    "keywords" : [ "south carolina" ],
    "statelongname" : "South Carolina"
  },
  "sd" : {
    "borders" : [ { "lat" : 43.06889, "lng" : -103.974609 },
      { "lat" : 42.940338, "lng" : -98.4375 },
      { "lat" : 42.553082, "lng" : -96.328125 },
      { "lat" : 45.951149, "lng" : -96.503906 },
      { "lat" : 46.073231, "lng" : -104.0625 },
      { "lat" : 43.06889, "lng" : -103.974609 } ],
    "keywords" : [ "south dakota" ],
    "statelongname" : "South Dakota"
  },
  "tn" : {
    "borders" : [ { "lat" : 36.527294, "lng" : -89.121094 },
      { "lat" : 36.527294, "lng" : -81.738281 },
      { "lat" : 34.957996, "lng" : -84.550781 },
      { "lat" : 35.101933, "lng" : -90.439453 },
      { "lat" : 36.527294, "lng" : -89.121094 } ],
    "keywords" : [ "tennessee", "memphis" ],
    "statelongname" : "Tennessee"
  },
  "tx" : {
    "borders" : [ { "lat" : 36.315125, "lng" : -103.007812 },
      { "lat" : 36.456635, "lng" : -100.107422 },
      { "lat" : 34.524662, "lng" : -100.019531 },
      { "lat" : 33.724339, "lng" : -96.855469 },
      { "lat" : 33.797409, "lng" : -95.537109 },
      { "lat" : 33.504761, "lng" : -93.955078 },
      { "lat" : 30.751278, "lng" : -93.691406 },
      { "lat" : 30.600094, "lng" : -92.988281 },
      { "lat" : 28.459032, "lng" : -96.943359 },
      { "lat" : 26.902477, "lng" : -97.734375 },
      { "lat" : 25.641525, "lng" : -97.119141 },
      { "lat" : 26.588528, "lng" : -99.404297 },
      { "lat" : 27.994402, "lng" : -99.755859 },
      { "lat" : 29.764378, "lng" : -101.425781 },
      { "lat" : 29.764378, "lng" : -102.744141 },
      { "lat" : 28.767658, "lng" : -103.095703 },
      { "lat" : 29.61167, "lng" : -104.501953 },
      { "lat" : 30.524412, "lng" : -105.117188 },
      { "lat" : 32.026707, "lng" : -106.611328 },
      { "lat" : 32.175613, "lng" : -102.919922 },
      { "lat" : 36.315125, "lng" : -103.007812 } ],
    "keywords" : [ "texas", "dallas", "houston", "san antonio", "cleveland" ],
    "statelongname" : "Texas"
  },
  "ut" : {
    "borders" : [ { "lat" : 41.967659, "lng" : -114.038086 },
      { "lat" : 37.125286, "lng" : -114.082031 },
      { "lat" : 37.09024, "lng" : -109.072266 },
      { "lat" : 41.013065, "lng" : -109.116211 },
      { "lat" : 41.046219, "lng" : -111.225586 },
      { "lat" : 42.032974, "lng" : -111.09375 },
      { "lat" : 41.967659, "lng" : -114.038086 } ],
    "keywords" : [ "utah" ],
    "statelongname" : "Utah"
  },
  "va" : {
    "borders" : [ { "lat" : 36.562599, "lng" : -83.891602 },
      { "lat" : 37.47485, "lng" : -82.045891 },
      { "lat" : 37.361427, "lng" : -81.760254 },
      { "lat" : 37.30027, "lng" : -81.430656 },
      { "lat" : 37.47485, "lng" : -80.288078 },
      { "lat" : 38.591114, "lng" : -79.639893 },
      { "lat" : 38.419167, "lng" : -79.420166 },
      { "lat" : 38.634037, "lng" : -79.189453 },
      { "lat" : 38.82259, "lng" : -79.024658 },
      { "lat" : 38.779781, "lng" : -78.815918 },
      { "lat" : 39.436192, "lng" : -78.299561 },
      { "lat" : 39.121536, "lng" : -77.871094 },
      { "lat" : 39.3088, "lng" : -77.684326 },
      { "lat" : 38.754082, "lng" : -76.948242 },
      { "lat" : 38.341648, "lng" : -77.387688 },
      { "lat" : 37.892189, "lng" : -76.113281 },
      { "lat" : 37.622932, "lng" : -76.376953 },
      { "lat" : 37.361427, "lng" : -76.289062 },
      { "lat" : 37.265308, "lng" : -76.508781 },
      { "lat" : 36.976227, "lng" : -76.223145 },
      { "lat" : 37.011326, "lng" : -75.827637 },
      { "lat" : 36.650791, "lng" : -75.959473 },
      { "lat" : 36.562599, "lng" : -83.891602 } ],
    "keywords" : [ "virginia", "hampton" ],
    "statelongname" : "Virginia"
  },
  "vi" : {
    "keywords" : [ "virgin islands" ],
    "statelongname" : "Virgin Islands"
  },
  "vt" : {
    "borders" : [ { "lat" : 42.763145, "lng" : -72.641602 },
      { "lat" : 42.795403, "lng" : -73.366699 },
      { "lat" : 43.659924, "lng" : -73.344727 },
      { "lat" : 44.182205, "lng" : -73.520508 },
      { "lat" : 45.026951, "lng" : -73.366699 },
      { "lat" : 45.026951, "lng" : -71.433105 },
      { "lat" : 44.699898, "lng" : -71.652832 },
      { "lat" : 44.433781, "lng" : -71.652832 },
      { "lat" : 44.276672, "lng" : -71.960449 },
      { "lat" : 43.628124, "lng" : -72.399902 },
      { "lat" : 42.763145, "lng" : -72.641602 } ],
    "keywords" : [ "vermont" ],
    "statelongname" : "Vermont"
  },
  "wa" : {
    "borders" : [ { "lat" : 48.400032, "lng" : -124.628906 },
      { "lat" : 45.8288, "lng" : -123.925781 },
      { "lat" : 46.134171, "lng" : -117.158203 },
      { "lat" : 48.980217, "lng" : -117.158203 },
      { "lat" : 48.922501, "lng" : -123.046875 },
      { "lat" : 48.224674, "lng" : -123.134766 },
      { "lat" : 48.400032, "lng" : -124.628906 } ],
    "keywords" : [ "washington", "seattle" ],
    "statelongname" : "Washington"
  },
  "wi" : {
    "borders" : [ { "lat" : 46.830135, "lng" : -92.06543 },
      { "lat" : 46.649437, "lng" : -90.351562 },
      { "lat" : 45.859413, "lng" : -87.93457 },
      { "lat" : 45.182037, "lng" : -87.583008 },
      { "lat" : 45.429298, "lng" : -86.923828 },
      { "lat" : 44.245197, "lng" : -87.670898 },
      { "lat" : 42.585445, "lng" : -87.978516 },
      { "lat" : 42.423458, "lng" : -90.65918 },
      { "lat" : 42.811523, "lng" : -91.098633 },
      { "lat" : 43.961189, "lng" : -91.318359 },
      { "lat" : 44.80912, "lng" : -92.8125 },
      { "lat" : 45.675484, "lng" : -92.900391 },
      { "lat" : 46.377254, "lng" : -92.15332 },
      { "lat" : 46.830135, "lng" : -92.06543 } ],
    "keywords" : [ "wisconsin", "milwaukee" ],
    "statelongname" : "Wisconsin"
  },
  "wv" : {
    "borders" : [ { "lat" : 39.842285, "lng" : -80.771484 },
      { "lat" : 39.732536, "lng" : -80.507812 },
      { "lat" : 39.707188, "lng" : -79.508057 },
      { "lat" : 39.698734, "lng" : -78.244629 },
      { "lat" : 38.81403, "lng" : -78.804932 },
      { "lat" : 38.82259, "lng" : -79.024658 },
      { "lat" : 38.444984, "lng" : -79.398193 },
      { "lat" : 38.599701, "lng" : -79.683838 },
      { "lat" : 37.474857, "lng" : -80.244141 },
      { "lat" : 37.309013, "lng" : -81.474609 },
      { "lat" : 37.483578, "lng" : -82.045898 },
      { "lat" : 38.125916, "lng" : -82.650146 },
      { "lat" : 38.350273, "lng" : -82.628174 },
      { "lat" : 38.444984, "lng" : -82.287598 },
      { "lat" : 38.993572, "lng" : -82.056885 },
      { "lat" : 39.842285, "lng" : -80.771484 } ],
    "keywords" : [ "west virginia" ],
    "statelongname" : "West Virginia"
  },
  "wy" : {
    "borders" : [ { "lat" : 41.145569, "lng" : -111.181641 },
      { "lat" : 40.979897, "lng" : -103.974609 },
      { "lat" : 45.058002, "lng" : -104.194336 },
      { "lat" : 45.151054, "lng" : -111.09375 },
      { "lat" : 41.145569, "lng" : -111.181641 } ],
    "keywords" : [ "wyoming" ],
    "statelongname" : "Wyoming"
  }
}

def scoreTweeterFeed(scores, json_line):
    if "text" in json_line:
        words = re.findall(r"[\w']+|[.,!?;]", json_line.get("text"))
        total_score = 0
        
        for word in words:
            if word in scores:
                total_score = total_score + scores.get(word)
        return total_score
    else:
        return 0    

def hw():
    afinnfile = open(sys.argv[1])
    scores = {} 
    for line in afinnfile:
        term, score  = line.lower().split("\t") 
        scores[term] = int(score)  
    afinnfile.close()

    tweeter_feed_file = open(sys.argv[2])
    
    state_scores = {}
    
    total_lines = 0
    filtered_us = 0
    associated_to_state = 0
    
    
    for line in tweeter_feed_file:
        json_feed = json.loads(line.lower())
        
        if json_feed.get("text") is None:
            continue
        
        total_lines = total_lines + 1
        
        score = scoreTweeterFeed(scores, json_feed)
        
        state = None
        if 'geo' in json_feed and json_feed['geo'] is not None:
            wrapper = json_feed['geo']
            if 'coordinates' in wrapper and wrapper['coordinates'] is not None:
                coordinates = wrapper['coordinates']
                state = findState(coordinates)
                
        if state is None:
            user = json_feed.get('user')
            if user is not None:
                utc_offset = user['utc_offset']
                timezone = user['time_zone']
                if utc_offset is not None and timezone is not None and utc_offset <= -14400 and utc_offset >= -36000:
                    filtered_us = filtered_us + 1
                    if 'hawaii' in timezone:
                        state = 'hi' 
                    elif 'arizona' in timezone:
                        state = 'az'
                    elif 'alaska' in timezone:
                        state = 'ak'
                    elif 'guam' in timezone:
                        state = 'gu'
                
                if state is None:
                    user_location = user['location']
                    if user_location is not None and user_location.strip():
                        temp_state = findStateKeyword(user_location)
                        if temp_state is not None:
                            state = temp_state
                        
        if state is not None:
            associated_to_state = associated_to_state + 1
            if state in state_scores:
                state_scores[state] = state_scores.get(state) + score
            else:
                state_scores[state] = score

    tweeter_feed_file.close()

    for state in sorted(state_scores, key = state_scores.__getitem__, reverse = True):
        print state
        break
    
    #print "---"
    
    #print "(A) Total Feeds = " + str(total_lines)
    #print "(B) Feeds filtered from US = " + str(filtered_us)
    #print "(C) Feeds from (B) were the state is derivable = " + str(associated_to_state)
    
    #state_derivation_success = float(associated_to_state) / filtered_us * 100
    #print "(D) Success of deriving state from US feed = " + str(state_derivation_success) + "%"
    
    #percent_filtered_out = float(filtered_us) / total_lines * 100
    #print "(E) Percent of A which is B = " + str(percent_filtered_out) + "%"
    
    #states_represented = len(state_scores)
    #percent_states_represented = float(states_represented) / len(states) * 100
    #print "(F) Number of states represented = " + str(states_represented)
    #print "(G) Percent of states represented = " + str(percent_states_represented) + "%"
    
    
def main():
    hw()
    
def hasBorderInfo(state):
    return 'borders' in states[state]
    
def getX(border_points, index):
    return border_points[index]['lat']
    
def getY(border_points, index):
    return border_points[index]['lng']
    
def inState(state, coord):
    border_points = states[state]['borders']
    j = len(border_points) - 2

    x = coord[0]
    y = coord[1]    
    oddNodes = False
    
    for i in range(0, j):
        polyX_i = getX(border_points, i)
        polyY_i = getY(border_points, i)

        polyX_j = getX(border_points, j)
        polyY_j = getY(border_points, j)

        if (polyY_i < y and polyY_j >= y) or (polyY_j < y and polyY_i >= y):
            if polyX_i + (y - polyY_i) / (polyY_j - polyY_i) * (polyX_j - polyX_i) < x:
                oddNodes = not oddNodes
        j = i;
        
    return oddNodes    
    
def hasStateKeywords(state, location):
    keywords = states[state]['keywords']
    for keyword in keywords:
        if keyword in location:
            return True
    return False

def findState(coord):
    for state in states:
        if hasBorderInfo(state):
            inStateResult = inState(state, coord)
            if inStateResult:
                return state
    return None

def findStateKeyword(location):
    for state in states:
        inStateResult = hasStateKeywords(state, location)
        if inStateResult:
            return state
    return None
    
        
if __name__ == "__main__":
    main()