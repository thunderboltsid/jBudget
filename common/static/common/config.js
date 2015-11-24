/**
 * Created by swozn on 9/19/2015.
 */
angular.module('eestec.common.config', [
    'ngMaterial'
])
    .config(["$mdThemingProvider", function ($mdThemingProvider) {
        $mdThemingProvider.definePalette('eestecred', {
            "50": "#fde9ea",
            "100": "#fabcbf",
            "200": "#f78f94",
            "300": "#f46a70",
            "400": "#f1444c",
            "500": "#ee1f28",
            "600": "#d01b23",
            "700": "#b3171e",
            "800": "#951319",
            "900": "#771014",
            "A100": "#fabcbf",
            "A200": "#f78f94",
            "A400": "#f1444c",
            "A700": "#b3171e"
        });

        $mdThemingProvider.definePalette('eestecgreen', {
            "50": "#e6fdf1",
            "100": "#b3f8d6",
            "200": "#80f3bb",
            "300": "#55eea4",
            "400": "#2aea8d",
            "500": "#00e676",
            "600": "#00c967",
            "700": "#00ad59",
            "800": "#00904a",
            "900": "#00733b",
            "A100": "#b3f8d6",
            "A200": "#80f3bb",
            "A400": "#2aea8d",
            "A700": "#00ad59"
        });

        $mdThemingProvider.definePalette('eestecgrey', {
            "50": "#e9e9e9",
            "100": "#bcbcbc",
            "200": "#909090",
            "300": "#6b6b6b",
            "400": "#464646",
            "500": "#212121",
            "600": "#1d1d1d",
            "700": "#191919",
            "800": "#151515",
            "900": "#111111",
            "A100": "#bcbcbc",
            "A200": "#909090",
            "A400": "#464646",
            "A700": "#191919"
        });

        $mdThemingProvider.theme('default')
            .primaryPalette('eestecred')
            .accentPalette('eestecgreen');
            //.backgroundPalette('eestecgrey');
    }]);
