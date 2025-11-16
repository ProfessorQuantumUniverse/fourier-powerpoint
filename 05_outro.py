"""
05_outro.py - Epic Closing Animation

Grand finale with:
- Waves and formulas filling the screen
- Fourier's portrait returning
- Powerful quote
- Name and dates
- Legacy summary
"""

from manim import *
import numpy as np


class OutroScene(Scene):
    """Epic closing scene bringing everything together"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Create background waves
        waves = VGroup()
        for i in range(8):
            frequency = i + 1
            amplitude = 0.5 / (i + 1)
            color = interpolate_color(BLUE, RED, i / 7)
            
            wave = FunctionGraph(
                lambda x, f=frequency, a=amplitude: a * np.sin(f * x),
                x_range=[-2*PI, 2*PI],
                color=color,
                stroke_width=2
            )
            wave.set_opacity(0.4)
            waves.add(wave)
        
        waves.arrange(DOWN, buff=0.3)
        
        # Start with waves appearing
        self.play(
            *[Create(wave, run_time=2) for wave in waves],
            lag_ratio=0.15
        )
        
        # Add wave motion
        for wave in waves:
            wave.add_updater(lambda m, dt: m.shift(RIGHT * dt * 0.3))
        
        self.wait(1)
        
        # Key formulas appear
        formulas = VGroup(
            MathTex(r"f(x) = \sum_{n=-\infty}^{\infty} c_n e^{inx}", font_size=36),
            MathTex(r"\frac{\partial u}{\partial t} = \alpha \nabla^2 u", font_size=36),
            MathTex(r"\hat{f}(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt", font_size=36),
        )
        
        formulas[0].set_color(BLUE).to_corner(UL).shift(DOWN * 0.5)
        formulas[1].set_color(RED).to_corner(UR).shift(DOWN * 0.5)
        formulas[2].set_color(YELLOW).to_edge(DOWN, buff=1)
        
        for formula in formulas:
            self.play(FadeIn(formula, scale=0.8), run_time=1)
            self.wait(0.3)
        
        self.wait(1)
        
        # Everything fades except waves
        self.play(
            *[FadeOut(formula) for formula in formulas],
            run_time=1
        )
        
        # Waves converge to center
        for wave in waves:
            wave.clear_updaters()
        
        self.play(
            *[wave.animate.move_to(ORIGIN).set_opacity(0.2) for wave in waves],
            run_time=2
        )
        
        # Portrait appears (or placeholder)
        try:
            portrait = SVGMobject("assets/fourier_portrait.svg")
            portrait.scale(2)
            has_portrait = True
        except:
            portrait = Circle(radius=2, color=WHITE, stroke_width=6)
            portrait_text = Text("J.F.", font_size=72, weight=BOLD)
            portrait_text.move_to(portrait.get_center())
            portrait = VGroup(portrait, portrait_text)
            has_portrait = False
        
        portrait.set_z_index(5)
        
        self.play(FadeIn(portrait, scale=0.5), run_time=1.5)
        self.wait(1)
        
        # Name appears
        name = Text("JOSEPH FOURIER", font_size=84, weight=BOLD)
        name.set_color_by_gradient(BLUE, PURPLE, RED)
        name.set_z_index(10)
        
        dates = Text("1768 - 1830", font_size=48, color=GRAY)
        dates.set_z_index(10)
        
        # Position text above and below portrait
        name.next_to(portrait, UP, buff=0.8)
        dates.next_to(portrait, DOWN, buff=0.8)
        
        self.play(
            Write(name, run_time=2),
            Write(dates, run_time=2)
        )
        self.wait(1)
        
        # Everything moves up to make room for quote
        everything = VGroup(portrait, name, dates)
        
        self.play(
            everything.animate.shift(UP * 1.5).scale(0.6),
            *[wave.animate.set_opacity(0.1) for wave in waves],
            run_time=1.5
        )
        
        # Famous quote appears
        quote = VGroup(
            Text('"', font_size=72, color=YELLOW),
            Text(
                "Nature is an inexhaustible source of truths",
                font_size=42,
                color=WHITE,
                slant=ITALIC
            ),
            Text('"', font_size=72, color=YELLOW),
        ).arrange(RIGHT, buff=0.2)
        
        quote.to_edge(DOWN, buff=1.5)
        quote.set_z_index(10)
        
        self.play(Write(quote, run_time=3))
        self.wait(2)
        
        # Final flourish - everything pulses
        self.play(
            everything.animate.scale(1.1),
            quote.animate.scale(1.1),
            *[wave.animate.set_opacity(0.3) for wave in waves],
            rate_func=there_and_back,
            run_time=2
        )
        
        self.wait(2)
        
        # Fade to black
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=3
        )
        
        self.wait(1)


class LegacyMontageScene(Scene):
    """Alternative ending showing the breadth of Fourier's legacy"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("The Legacy", font_size=96, weight=BOLD)
        title.set_color_by_gradient(GOLD, YELLOW, ORANGE)
        
        self.play(Write(title, run_time=2))
        self.wait(1)
        
        self.play(title.animate.scale(0.6).to_edge(UP, buff=0.5), run_time=1)
        
        # Show impact areas radiating out
        impacts = [
            ("Mathematics", BLUE, UP + LEFT * 2),
            ("Physics", RED, UP + RIGHT * 2),
            ("Engineering", GREEN, DOWN + RIGHT * 2),
            ("Medicine", TEAL, DOWN + LEFT * 2),
            ("Technology", PURPLE, LEFT * 3),
            ("Communications", PINK, RIGHT * 3),
        ]
        
        impact_texts = VGroup()
        
        for impact, color, direction in impacts:
            text = Text(impact, font_size=40, color=color, weight=BOLD)
            text.move_to(direction)
            impact_texts.add(text)
            
            # Lines connecting to center
            line = Line(ORIGIN, text.get_center(), color=color, stroke_width=3)
            line.set_opacity(0.5)
            
            self.play(
                Create(line),
                FadeIn(text, shift=-direction/2),
                run_time=0.8
            )
            self.wait(0.2)
        
        # Center element
        center = Dot(ORIGIN, radius=0.3, color=YELLOW)
        center_label = Text("Fourier", font_size=32, color=YELLOW)
        center_label.next_to(center, DOWN, buff=0.3)
        
        self.play(
            GrowFromCenter(center),
            Write(center_label),
            run_time=1
        )
        
        self.wait(2)
        
        # Fade out for next section
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        self.wait(0.5)


class WaveConvergenceScene(Scene):
    """Waves converging into a single beautiful form"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Create many waves from all directions
        waves = VGroup()
        
        # From top
        for i in range(5):
            wave = FunctionGraph(
                lambda x: 0.3 * np.sin((i+1) * x),
                x_range=[-3, 3],
                color=interpolate_color(BLUE, PURPLE, i/4),
                stroke_width=3
            )
            wave.shift(UP * 3 + RIGHT * (i - 2))
            waves.add(wave)
        
        # From bottom
        for i in range(5):
            wave = FunctionGraph(
                lambda x: 0.3 * np.cos((i+1) * x),
                x_range=[-3, 3],
                color=interpolate_color(RED, ORANGE, i/4),
                stroke_width=3
            )
            wave.shift(DOWN * 3 + RIGHT * (i - 2))
            waves.add(wave)
        
        # From left
        for i in range(4):
            wave = FunctionGraph(
                lambda x: 0.3 * np.sin((i+1) * x),
                x_range=[-2, 2],
                color=interpolate_color(GREEN, TEAL, i/3),
                stroke_width=3
            )
            wave.rotate(PI/2)
            wave.shift(LEFT * 5 + UP * (i - 1.5))
            waves.add(wave)
        
        # From right
        for i in range(4):
            wave = FunctionGraph(
                lambda x: 0.3 * np.cos((i+1) * x),
                x_range=[-2, 2],
                color=interpolate_color(YELLOW, PINK, i/3),
                stroke_width=3
            )
            wave.rotate(-PI/2)
            wave.shift(RIGHT * 5 + UP * (i - 1.5))
            waves.add(wave)
        
        # Create all waves
        self.play(*[Create(wave) for wave in waves], run_time=2, lag_ratio=0.05)
        self.wait(0.5)
        
        # Converge to center
        self.play(
            *[wave.animate.move_to(ORIGIN).set_opacity(0.4) for wave in waves],
            run_time=3,
            rate_func=smooth
        )
        
        self.wait(1)
        
        # Form a beautiful mandala pattern
        for i, wave in enumerate(waves):
            angle = (i / len(waves)) * 2 * PI
            radius = 2
            wave.generate_target()
            wave.target.rotate(angle)
            wave.target.shift(radius * np.cos(angle) * RIGHT + radius * np.sin(angle) * UP)
            wave.target.set_opacity(0.7)
        
        self.play(*[MoveToTarget(wave) for wave in waves], run_time=2)
        
        # Rotate the whole pattern
        for wave in waves:
            wave.add_updater(lambda m, dt: m.rotate(dt * 0.5))
        
        self.wait(3)
        
        # Stop rotation
        for wave in waves:
            wave.clear_updaters()
        
        # Final text
        final_text = Text(
            "Forever Transforming Our World",
            font_size=56,
            weight=BOLD
        )
        final_text.set_color_by_gradient(BLUE, PURPLE, PINK)
        final_text.set_z_index(10)
        
        self.play(Write(final_text), run_time=2)
        self.wait(2)
        
        # Fade all
        self.play(
            *[FadeOut(wave) for wave in waves],
            FadeOut(final_text),
            run_time=3
        )
        
        self.wait(1)


class FullOutroSequence(Scene):
    """Complete outro sequence - use this for final video"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Part 1: Waves gathering
        self.show_waves_gathering()
        
        # Part 2: Portrait and name
        self.show_portrait_and_name()
        
        # Part 3: Quote
        self.show_quote()
        
        # Part 4: Legacy items
        self.show_legacy()
        
        # Part 5: Final fade
        self.final_fade()
    
    def show_waves_gathering(self):
        """Create dramatic wave convergence"""
        waves = VGroup()
        for i in range(12):
            freq = i + 1
            amp = 0.4 / np.sqrt(i + 1)
            color = interpolate_color(BLUE, RED, i / 11)
            
            wave = FunctionGraph(
                lambda x, f=freq, a=amp: a * np.sin(f * x),
                x_range=[-3*PI, 3*PI],
                color=color,
                stroke_width=2
            )
            wave.shift(UP * (i - 5.5) * 0.6)
            waves.add(wave)
        
        self.play(*[Create(wave) for wave in waves], run_time=2.5, lag_ratio=0.1)
        self.wait(0.5)
        
        # Converge
        self.play(
            *[wave.animate.move_to(ORIGIN).set_opacity(0.2) for wave in waves],
            run_time=2
        )
        
        self.waves = waves
    
    def show_portrait_and_name(self):
        """Show portrait with name and dates"""
        try:
            portrait = SVGMobject("assets/fourier_portrait.svg").scale(2.5)
        except:
            portrait = Circle(radius=2.5, color=WHITE, stroke_width=6, fill_opacity=0.1)
        
        portrait.set_z_index(5)
        
        self.play(FadeIn(portrait, scale=0.5), run_time=1.5)
        
        name = Text("JOSEPH FOURIER", font_size=96, weight=BOLD)
        name.set_color_by_gradient(BLUE, PURPLE, RED)
        name.next_to(portrait, UP, buff=1)
        name.set_z_index(10)
        
        dates = Text("1768 - 1830", font_size=56, color=GOLD)
        dates.next_to(portrait, DOWN, buff=1)
        dates.set_z_index(10)
        
        self.play(Write(name, run_time=2))
        self.play(Write(dates, run_time=1.5))
        self.wait(2)
        
        self.portrait = portrait
        self.name = name
        self.dates = dates
    
    def show_quote(self):
        """Display memorable quote"""
        everything = VGroup(self.portrait, self.name, self.dates)
        
        self.play(
            everything.animate.scale(0.5).to_edge(UP, buff=0.5),
            *[wave.animate.set_opacity(0.1) for wave in self.waves],
            run_time=1.5
        )
        
        quote = Text(
            '"Nature is an inexhaustible\nsource of truths"',
            font_size=52,
            color=YELLOW,
            slant=ITALIC,
            line_spacing=1.3
        )
        quote.set_z_index(10)
        quote.shift(DOWN * 0.5)
        
        self.play(FadeIn(quote, scale=1.2), run_time=2)
        self.wait(3)
        
        self.quote = quote
    
    def show_legacy(self):
        """Show key legacy items"""
        legacy_items = VGroup(
            Text("• Fourier Series", font_size=32),
            Text("• Heat Equation", font_size=32),
            Text("• Fourier Transform", font_size=32),
            Text("• Modern Technology", font_size=32),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        legacy_items.set_color_by_gradient(BLUE, PURPLE, PINK)
        legacy_items.next_to(self.quote, DOWN, buff=0.8)
        legacy_items.set_z_index(10)
        
        for item in legacy_items:
            self.play(FadeIn(item, shift=UP), run_time=0.6)
            self.wait(0.2)
        
        self.wait(2)
        self.legacy_items = legacy_items
    
    def final_fade(self):
        """Epic fade to black"""
        # Pulse everything one last time
        all_mobjects = VGroup(*self.mobjects)
        
        self.play(
            all_mobjects.animate.scale(1.1),
            *[wave.animate.set_opacity(0.3) for wave in self.waves],
            rate_func=there_and_back,
            run_time=2
        )
        
        self.wait(1)
        
        # Slow fade to black
        self.play(
            *[FadeOut(mob, run_time=4) for mob in self.mobjects]
        )
        
        self.wait(2)
