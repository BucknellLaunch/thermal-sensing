function createGraph(data, status, request) {
    var graph = new Rickshaw.Graph({
    element: document.querySelector("#chart"),
    width: 900,
    height: 600,
    renderer: 'line',
    min: -4,
    max: 4,
    series: data
    });

    var y_ticks = new Rickshaw.Graph.Axis.Y({
        graph: graph,
        orientation: 'right',
        tickFormat: Rickshaw.Fixtures.Number.formatKMBT,
        pixelsPerTick: 60,
        element: document.getElementById('y_axis'),
    });

    graph.render();

    var x_axis = new Rickshaw.Graph.Axis.Time({
        graph: graph
    });

    x_axis.render();

    var hoverDetail = new Rickshaw.Graph.HoverDetail({
        graph: graph
    });

    var legend = new Rickshaw.Graph.Legend({
        graph: graph,
        element: document.getElementById('legend')
    });

    var shelving = new Rickshaw.Graph.Behavior.Series.Toggle({
        graph: graph,
        legend: legend
    });

    var highlighter = new Rickshaw.Graph.Behavior.Series.Highlight({
        graph: graph,
        legend: legend
    });

    var slider = new Rickshaw.Graph.RangeSlider({
    graph: graph,
    element: document.getElementById('slider')
    });
}

$.ajax({
    dataType: 'json',
    url: 'api/graph',
    success: createGraph
});