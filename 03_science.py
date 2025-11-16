"""
03_science.py - Fourier's Scientific Contributions

This script contains animations for Fourier's most important scientific ideas:
- Fourier Series
- Fourier Transform
- Heat Equation
- Wave decomposition
"""

from manim import *
import numpy as np


class FourierSeriesScene(Scene):
    """Demonstrate the Fourier Series concept with square wave approximation"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("Fourier Series", font_size=72, weight=BOLD)
        title.set_color_by_gradient(BLUE, PURPLE)
        title.to_edge(UP, buff=0.3)
        
        subtitle = Text(
            "Any periodic function can be represented as a sum of sine and cosine waves",
            font_size=28,
            color=GRAY
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        
        # Show title
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(0.5)
        
        # Create axes
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": GRAY},
            tips=False
        )
        axes.shift(DOWN * 0.5)
        
        # Target function (square wave)
        target_func = axes.plot(
            lambda x: 1 if np.sin(x) > 0 else -1,
            color=WHITE,
            stroke_width=4,
            discontinuities=[-PI, 0, PI]
        )
        target_label = Text("Target: Square Wave", font_size=32, color=WHITE)
        target_label.next_to(axes, DOWN, buff=0.5)
        
        self.play(FadeOut(title), FadeOut(subtitle))
        self.play(Create(axes), run_time=1.5)
        self.play(Create(target_func), Write(target_label), run_time=1.5)
        self.wait(1)
        
        # Build up Fourier series approximation
        self.play(FadeOut(target_func), FadeOut(target_label))
        
        # Show individual sine components
        approximations = []
        formulas = []
        
        n_terms = [1, 3, 5, 7, 9]
        
        for n in n_terms:
            # Formula for this term
            formula = MathTex(
                rf"\frac{{4}}{{\pi}} \sin({n}x) / {n}",
                font_size=36,
                color=interpolate_color(BLUE, RED, n / 10)
            )
            formula.to_corner(UR)
            formulas.append(formula)
            
            # Individual sine wave
            sine_wave = axes.plot(
                lambda x: (4 / np.pi) * np.sin(n * x) / n,
                color=interpolate_color(BLUE, RED, n / 10),
                stroke_width=3
            )
            
            # Show the component
            self.play(
                Write(formula),
                Create(sine_wave),
                run_time=1
            )
            self.wait(0.5)
            
            approximations.append(sine_wave)
        
        # Clear individual components
        self.wait(0.5)
        self.play(
            *[FadeOut(f) for f in formulas],
            *[FadeOut(a) for a in approximations],
            run_time=1
        )
        
        # Show progressive approximation
        approximation_label = Text("Building Approximation...", font_size=36)
        approximation_label.to_edge(DOWN, buff=0.5)
        self.play(Write(approximation_label))
        
        for i, n in enumerate([1, 2, 3, 5, 7, 9, 11, 15, 19, 25]):
            # Fourier series approximation with n terms
            def approx_func(x):
                total = 0
                for k in range(1, n+1, 2):  # odd harmonics only for square wave
                    total += (4 / np.pi) * np.sin(k * x) / k
                return total
            
            approx_wave = axes.plot(
                approx_func,
                color=YELLOW,
                stroke_width=4
            )
            
            n_label = Text(f"n = {n} terms", font_size=32, color=YELLOW)
            n_label.next_to(axes, DOWN, buff=0.3)
            
            if i == 0:
                self.play(
                    Create(approx_wave),
                    FadeIn(n_label),
                    FadeOut(approximation_label),
                    run_time=0.8
                )
            else:
                self.play(
                    ReplacementTransform(prev_wave, approx_wave),
                    ReplacementTransform(prev_label, n_label),
                    run_time=0.6
                )
            
            prev_wave = approx_wave
            prev_label = n_label
            self.wait(0.3)
        
        # Show target function again for comparison
        self.play(Create(target_func), run_time=1)
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)


class HeatEquationScene(Scene):
    """Visualize the heat equation and Fourier's contribution"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("The Heat Equation", font_size=72, weight=BOLD)
        title.set_color_by_gradient(RED, ORANGE, YELLOW)
        title.to_edge(UP, buff=0.3)
        
        subtitle = Text("Fourier's Revolutionary Contribution", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(1)
        
        # Show the heat equation
        heat_eq = MathTex(
            r"\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}",
            font_size=72
        )
        heat_eq.set_color_by_gradient(RED, ORANGE, YELLOW)
        
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            Write(heat_eq),
            run_time=2
        )
        self.wait(1.5)
        
        # Explain components
        explanations = VGroup(
            MathTex(r"\frac{\partial u}{\partial t}", color=RED, font_size=48),
            Text("Rate of temperature change", font_size=28, color=GRAY),
            MathTex(r"\alpha", color=ORANGE, font_size=48),
            Text("Thermal diffusivity", font_size=28, color=GRAY),
            MathTex(r"\frac{\partial^2 u}{\partial x^2}", color=YELLOW, font_size=48),
            Text("Spatial curvature", font_size=28, color=GRAY),
        )
        
        # Position explanations in three columns
        col1 = VGroup(explanations[0], explanations[1]).arrange(DOWN, buff=0.2)
        col2 = VGroup(explanations[2], explanations[3]).arrange(DOWN, buff=0.2)
        col3 = VGroup(explanations[4], explanations[5]).arrange(DOWN, buff=0.2)
        
        cols = VGroup(col1, col2, col3).arrange(RIGHT, buff=1.5)
        cols.next_to(heat_eq, DOWN, buff=1)
        
        self.play(heat_eq.animate.to_edge(UP, buff=1), run_time=1)
        self.play(*[FadeIn(col, shift=UP) for col in cols], run_time=1.5)
        self.wait(2)
        
        # Clear for visualization
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1)
        
        # Visual heat diffusion
        title2 = Text("Heat Diffusion Over Time", font_size=56)
        title2.set_color_by_gradient(RED, YELLOW)
        title2.to_edge(UP, buff=0.3)
        self.play(Write(title2))
        
        # Create a bar representing a metal rod
        rod = Rectangle(width=10, height=0.8, color=WHITE, stroke_width=3)
        rod.shift(DOWN * 0.5)
        
        # Create heat distribution representation
        num_segments = 50
        segments = VGroup()
        
        for i in range(num_segments):
            segment = Rectangle(
                width=10/num_segments,
                height=0.8,
                stroke_width=0,
                fill_opacity=0.8
            )
            segment.move_to(rod.get_left() + RIGHT * (i * 10/num_segments + 5/num_segments))
            segments.add(segment)
        
        self.play(Create(rod), run_time=1)
        self.wait(0.5)
        
        # Animate heat diffusion
        time_label = Text("t = 0", font_size=36, color=GRAY)
        time_label.next_to(rod, DOWN, buff=0.5)
        self.play(Write(time_label))
        
        # Initial condition: hot in the middle
        for t in np.linspace(0, 5, 60):
            for i, segment in enumerate(segments):
                x = (i - num_segments/2) / (num_segments/2)
                # Heat equation solution approximation
                temp = np.exp(-x**2 / (1 + 0.5*t))
                color = interpolate_color(BLUE, RED, temp)
                segment.set_fill(color, opacity=0.8)
            
            new_label = Text(f"t = {t:.1f}", font_size=36, color=GRAY)
            new_label.next_to(rod, DOWN, buff=0.5)
            
            if t > 0:
                time_label.become(new_label)
            
            self.wait(0.05)
        
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)


class FourierTransformScene(Scene):
    """Introduce the Fourier Transform concept"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("The Fourier Transform", font_size=72, weight=BOLD)
        title.set_color_by_gradient(BLUE, GREEN, YELLOW)
        title.to_edge(UP, buff=0.3)
        
        subtitle = Text(
            "From Time Domain to Frequency Domain",
            font_size=32,
            color=GRAY
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(1)
        
        # Fourier Transform formula
        ft_formula = MathTex(
            r"\hat{f}(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt",
            font_size=60
        )
        ft_formula.set_color_by_gradient(BLUE, PURPLE)
        
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            Write(ft_formula),
            run_time=2
        )
        self.wait(1.5)
        
        self.play(ft_formula.animate.scale(0.7).to_edge(UP, buff=0.5), run_time=1)
        
        # Show time domain signal
        time_label = Text("Time Domain", font_size=40, color=BLUE)
        time_label.to_corner(UL).shift(DOWN * 2)
        
        axes_time = Axes(
            x_range=[0, 4, 1],
            y_range=[-2, 2, 1],
            x_length=5,
            y_length=3,
            axis_config={"color": GRAY}
        ).shift(LEFT * 3 + DOWN * 0.5)
        
        # Complex signal (sum of frequencies)
        signal = axes_time.plot(
            lambda t: np.sin(2*PI*t) + 0.5*np.sin(2*PI*3*t) + 0.3*np.sin(2*PI*5*t),
            color=BLUE,
            stroke_width=3
        )
        
        self.play(Write(time_label))
        self.play(Create(axes_time), run_time=1)
        self.play(Create(signal), run_time=2)
        self.wait(1)
        
        # Show frequency domain
        freq_label = Text("Frequency Domain", font_size=40, color=GREEN)
        freq_label.to_corner(UR).shift(DOWN * 2)
        
        axes_freq = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 1.5, 0.5],
            x_length=5,
            y_length=3,
            axis_config={"color": GRAY}
        ).shift(RIGHT * 3 + DOWN * 0.5)
        
        # Frequency peaks
        peak1 = axes_freq.plot_line_graph(
            x_values=[1, 1],
            y_values=[0, 1],
            add_vertex_dots=False,
            line_color=GREEN,
            stroke_width=6
        )
        
        peak2 = axes_freq.plot_line_graph(
            x_values=[3, 3],
            y_values=[0, 0.5],
            add_vertex_dots=False,
            line_color=GREEN,
            stroke_width=6
        )
        
        peak3 = axes_freq.plot_line_graph(
            x_values=[5, 5],
            y_values=[0, 0.3],
            add_vertex_dots=False,
            line_color=GREEN,
            stroke_width=6
        )
        
        # Arrow between domains
        arrow = Arrow(
            start=axes_time.get_right() + RIGHT * 0.3,
            end=axes_freq.get_left() + LEFT * 0.3,
            color=YELLOW,
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        arrow_label = Text("Transform", font_size=28, color=YELLOW)
        arrow_label.next_to(arrow, UP)
        
        self.play(Write(freq_label))
        self.play(Create(axes_freq), run_time=1)
        self.wait(0.5)
        
        self.play(GrowArrow(arrow), Write(arrow_label), run_time=1.5)
        self.wait(0.5)
        
        # Show frequency components appearing
        self.play(Create(peak1), run_time=0.8)
        self.wait(0.3)
        self.play(Create(peak2), run_time=0.8)
        self.wait(0.3)
        self.play(Create(peak3), run_time=0.8)
        
        self.wait(2)
        
        # Highlight the insight
        insight = Text(
            "Hidden frequencies revealed!",
            font_size=48,
            color=YELLOW,
            weight=BOLD
        )
        insight.to_edge(DOWN, buff=0.5)
        
        self.play(Write(insight), run_time=1.5)
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)


class WaveDecompositionScene(Scene):
    """Show how complex waves decompose into simple components"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        title = Text("Wave Decomposition", font_size=64, weight=BOLD)
        title.set_color_by_gradient(BLUE, PURPLE, RED)
        title.to_edge(UP, buff=0.3)
        
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # Create complex wave
        axes = Axes(
            x_range=[0, 4*PI, PI],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": GRAY}
        )
        
        # Components
        wave1 = axes.plot(lambda x: np.sin(x), color=RED, stroke_width=2)
        wave2 = axes.plot(lambda x: 0.5*np.sin(2*x), color=GREEN, stroke_width=2)
        wave3 = axes.plot(lambda x: 0.33*np.sin(3*x), color=BLUE, stroke_width=2)
        
        # Combined wave
        combined = axes.plot(
            lambda x: np.sin(x) + 0.5*np.sin(2*x) + 0.33*np.sin(3*x),
            color=YELLOW,
            stroke_width=4
        )
        
        # Show combined wave first
        self.play(FadeOut(title))
        self.play(Create(axes))
        self.play(Create(combined), run_time=2)
        
        label_combined = Text("Complex Wave", font_size=36, color=YELLOW)
        label_combined.to_edge(DOWN)
        self.play(Write(label_combined))
        self.wait(1)
        
        # "Explode" into components
        self.play(FadeOut(label_combined))
        
        component_label = Text("Fourier Components:", font_size=36)
        component_label.to_edge(DOWN)
        self.play(Write(component_label))
        
        self.play(
            combined.animate.set_opacity(0.3),
            Create(wave1),
            Create(wave2),
            Create(wave3),
            run_time=2
        )
        
        # Labels for components
        labels = VGroup(
            MathTex(r"\sin(x)", color=RED),
            MathTex(r"\frac{1}{2}\sin(2x)", color=GREEN),
            MathTex(r"\frac{1}{3}\sin(3x)", color=BLUE),
        ).arrange(RIGHT, buff=0.5)
        labels.next_to(component_label, UP, buff=0.3)
        
        self.play(Write(labels), run_time=1.5)
        self.wait(2)
        
        # Recombine
        self.play(
            FadeOut(wave1),
            FadeOut(wave2),
            FadeOut(wave3),
            combined.animate.set_opacity(1),
            FadeOut(labels),
            FadeOut(component_label),
            run_time=2
        )
        
        self.wait(1)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)
