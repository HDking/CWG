/*jslint */
/*global AdobeEdge: false, window: false, document: false, console:false, alert: false */
(function (compId) {

    "use strict";
    var im='images/',
        aud='media/',
        vid='media/',
        js='js/',
        fonts = {
            'allura, cursive': '<script src=\"http://use.edgefonts.net/allura:n4:all.js\"></script>',
            'iceland, sans-serif': '<script src=\"http://use.edgefonts.net/iceland:n4:all.js\"></script>'        },
        opts = {
            'gAudioPreloadPreference': 'auto',
            'gVideoPreloadPreference': 'auto'
        },
        resources = [
        ],
        scripts = [
            js+"jquery-1.7.1.min.js"
        ],
        symbols = {
            "stage": {
                version: "6.0.0",
                minimumCompatibleVersion: "5.0.0",
                build: "6.0.0.400",
                scaleToFit: "none",
                centerStage: "none",
                resizeInstances: false,
                content: {
                    dom: [
                        {
                            id: '_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_BG',
                            type: 'image',
                            rect: ['0px', '0px', '1024px', '122px', 'auto', 'auto'],
                            cursor: 'pointer',
                            fill: ["rgba(0,0,0,0)",im+"021_FD_GREENQUEST_MISSIE%2007%20FASE%2001_BANNER%201024x122%20PX_BG.jpg",'0px','0px'],
                            transform: [[],[],[],['1.1','1.1']]
                        },
                        {
                            id: '_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_WhteL2',
                            type: 'image',
                            rect: ['70px', '11px', '467px', '102px', 'auto', 'auto'],
                            cursor: 'pointer',
                            fill: ["rgba(0,0,0,0)",im+"021_FD_GREENQUEST_MISSIE%2007%20FASE%2001_BANNER%201024x122%20PX_WhteL2.png",'0px','0px'],
                            filter: [0, 0, 1, 1, 0, 0, 0, 0, "rgba(0,0,0,0)", 0, 0, 0]
                        },
                        {
                            id: '_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_WhteR2',
                            type: 'image',
                            rect: ['573px', '-131px', '295px', '102px', 'auto', 'auto'],
                            cursor: 'pointer',
                            fill: ["rgba(0,0,0,0)",im+"021_FD_GREENQUEST_MISSIE%2007%20FASE%2001_BANNER%201024x122%20PX_WhteR2.png",'0px','0px'],
                            filter: [0, 0, 1, 1, 0, 0, 0, 0, "rgba(0,0,0,0)", 0, 0, 0]
                        },
                        {
                            id: 'Text4',
                            type: 'text',
                            rect: ['588px', '23px', '265px', '48px', 'auto', 'auto'],
                            text: "<p style=\"margin: 0px;\">​</p>",
                            align: "left",
                            font: ['Verdana, Geneva, sans-serif', [32, "px"], "rgba(0,0,0,1)", "700", "none", "normal", "break-word", "normal"],
                            textStyle: ["", "", "", "", "uppercase"]
                        },
                        {
                            id: 'Rectangle',
                            type: 'rect',
                            rect: ['0px', '0px', '1024px', '122px', 'auto', 'auto'],
                            opacity: '1',
                            fill: ["rgba(255,255,255,1.00)"],
                            stroke: [0,"rgba(0,0,0,1)","none"]
                        },
                        {
                            id: 'Rectangle2',
                            type: 'rect',
                            rect: ['594px', '-113px', '254px', '39px', 'auto', 'auto'],
                            opacity: '1',
                            fill: ["rgba(255,255,255,1.00)"],
                            stroke: [0,"rgba(0,0,0,1)","none"]
                        }
                    ],
                    style: {
                        '${Stage}': {
                            isStage: true,
                            rect: ['null', 'null', '1024px', '122px', 'auto', 'auto'],
                            sizeRange: ['0px','','',''],
                            overflow: 'hidden',
                            fill: ["rgba(255,255,255,1.00)",[270,[['rgba(255,255,255,0.00)',0],['rgba(255,255,255,0.00)',100]]]]
                        }
                    }
                },
                timeline: {
                    duration: 5000,
                    autoPlay: true,
                    labels: {
                        "Label 1": 0
                    },
                    data: [
                        [
                            "eid157",
                            "top",
                            3250,
                            1185,
                            "easeOutQuad",
                            "${Rectangle2}",
                            '-113px',
                            '28px'
                        ],
                        [
                            "eid148",
                            "opacity",
                            0,
                            1500,
                            "easeInQuad",
                            "${Rectangle}",
                            '1',
                            '0'
                        ],
                        [
                            "eid110",
                            "top",
                            3250,
                            1185,
                            "easeOutQuad",
                            "${_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_WhteR2}",
                            '-131px',
                            '10px'
                        ],
                        [
                            "eid100",
                            "height",
                            0,
                            0,
                            "linear",
                            "${Stage}",
                            '122px',
                            '122px'
                        ],
                        [
                            "eid85",
                            "background-image",
                            0,
                            0,
                            "linear",
                            "${Stage}",
                            [270,[['rgba(255,255,255,0.00)',0],['rgba(255,255,255,0.00)',100]]],
                            [270,[['rgba(255,255,255,0.00)',0],['rgba(255,255,255,0.00)',100]]]
                        ],
                        [
                            "eid149",
                            "background-color",
                            0,
                            0,
                            "easeOutQuad",
                            "${Rectangle}",
                            'rgba(255,255,255,1.00)',
                            'rgba(255,255,255,1.00)'
                        ],
                        [
                            "eid156",
                            "opacity",
                            4435,
                            565,
                            "linear",
                            "${Rectangle2}",
                            '1',
                            '0'
                        ],
                        [
                            "eid101",
                            "background-color",
                            0,
                            0,
                            "easeOutQuad",
                            "${Stage}",
                            'rgba(255,255,255,1.00)',
                            'rgba(255,255,255,1.00)'
                        ],
                        [
                            "eid144",
                            "scaleY",
                            0,
                            4435,
                            "easeOutQuad",
                            "${_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_BG}",
                            '1',
                            '1.1'
                        ],
                        [
                            "eid133",
                            "filter.blur",
                            3250,
                            0,
                            "easeOutQuad",
                            "${_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_WhteR2}",
                            '0px',
                            '0px'
                        ],
                        [
                            "eid134",
                            "filter.blur",
                            4435,
                            0,
                            "easeOutQuad",
                            "${_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_WhteR2}",
                            '0px',
                            '0px'
                        ],
                        [
                            "eid143",
                            "scaleX",
                            0,
                            4435,
                            "easeOutQuad",
                            "${_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_BG}",
                            '1',
                            '1.1'
                        ],
                        [
                            "eid158",
                            "width",
                            0,
                            0,
                            "easeOutQuad",
                            "${Stage}",
                            '1024px',
                            '1024px'
                        ],
                        [
                            "eid131",
                            "filter.blur",
                            1750,
                            0,
                            "easeOutQuad",
                            "${_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_WhteL2}",
                            '0px',
                            '0px'
                        ],
                        [
                            "eid132",
                            "filter.blur",
                            3385,
                            0,
                            "easeOutQuad",
                            "${_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_WhteL2}",
                            '0px',
                            '0px'
                        ],
                        [
                            "eid129",
                            "left",
                            1750,
                            1635,
                            "easeOutQuad",
                            "${_021_FD_GREENQUEST_MISSIE_07_FASE_01_BANNER_1024x122_PX_WhteL2}",
                            '-480px',
                            '97px'
                        ]
                    ]
                }
            }
        };

    AdobeEdge.registerCompositionDefn(compId, symbols, fonts, scripts, resources, opts);

    if (!window.edge_authoring_mode) AdobeEdge.getComposition(compId).load("tests4_edgeActions.js");
})("EDGE-4698296");
