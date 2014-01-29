/* Rickshaw example */
var dataSet1 = [
	{ x: 0, y: 40 },
	{ x: 1, y: 49 },
	{ x: 2, y: 17 },
	{ x: 3, y: 42 }
];

var dataSet2 = [
	{ x: 0, y: 50 },
	{ x: 1, y: 11 },
	{ x: 2, y: 21 },
	{ x: 3, y: 60 }
];

var palette = new Rickshaw.Color.Palette();

var graph = new Rickshaw.Graph( {
	element: document.querySelector("#chart"),
	width: 580,
	height: 250,
	series: [
		{
			name: 'Blue Data',
			color: palette.color(),
			data: dataSet1
		},
		{
			name: 'Red Data',
			color: palette.color(),
			data: dataSet2
		}
		]
} );

var legend = new Rickshaw.Graph.Legend( {
	element: document.querySelector("#legend"),
	graph: graph
});

graph.render();