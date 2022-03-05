from manim import BLACK, Scene, config
from manim.mobject.geometry.line import Arrow, Line
from manim.mobject.graph import Graph
from manim.mobject.text.tex_mobject import Tex


class ExampleDiagram(Scene):
    config.transparent = True
    config.output_file = 'example_diagram'

    def graph(
        self, nodes: list[int], edges: list[tuple[int, int]], **kwargs
    ) -> Graph:
        _graph = Graph(
            vertices=nodes,
            edges=edges,
            labels={i: Tex(i, font_size=80, color=BLACK) for i in nodes},
            vertex_config={'radius': 0.75, 'color': '#FFA724'},
            edge_type=Arrow,
            edge_config={'buff': 0.7, 'stroke_width': 6, 'color': '#FFA724'},
            **kwargs
        )

        return _graph

    def construct(self) -> None:
        g1 = self.graph(
            [2, 4, 3],
            [(2, 4), (4, 3)],
            layout={2: [-3.5, 2, 0], 4: [0, 2, 0], 3: [3.5, 2, 0]},
        )
        g2 = self.graph(
            [5, 6, 4],
            [(5, 6), (6, 4)],
            layout={5: [-3.5, 0, 0], 6: [0, 0, 0], 4: [3.5, 0, 0]},
        )
        g3 = self.graph(
            [7, 0, 8],
            [(7, 0), (0, 8)],
            layout={7: [-3.5, -2, 0], 0: [0, -2, 0], 8: [3.5, -2, 0]},
        )

        self.add(g1)
        self.add(g2)
        self.add(
            Line(
                color='#FFA724',
                stroke_width=6,
                start=[-4.25, 0, 0],
                end=[4.25, 0, 0],
            ).move_to(sum(i.get_center() for i in [g2, g3]) / 2)
        )
        self.add(g3)
