"""
01_intro.py - Epic Opening Animation for Joseph Fourier Presentation

This scene creates an epic introduction with:
- Fourier's name appearing dramatically
- Animated waves and formulas
- Portrait integration (if available)
- Building anticipation for the presentation
"""

from manim import *
import numpy as np


class IntroScene(Scene):
    """Epic opening scene with name, waves, and formulas"""
    
    def construct(self):
        # Set background color to dark
        self.camera.background_color = "#0a0a0a"
        
        # Create epic title
        title = Text("JOSEPH FOURIER", font_size=96, weight=BOLD)
        title.set_color_by_gradient(BLUE, PURPLE, RED)
        
        subtitle = Text("1768 - 1830", font_size=48)
        subtitle.set_color(GRAY)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        # Create decorative waves in background
        waves = VGroup()
        for i in range(5):
            wave = self.create_fourier_wave(
                frequency=i + 1,
                amplitude=0.3,
                color=interpolate_color(BLUE, RED, i / 4)
            )
            wave.set_opacity(0.3)
            waves.add(wave)
        
        # Position waves
        waves.arrange(DOWN, buff=0.2)
        waves.to_edge(LEFT, buff=0.5)
        
        # Create Fourier series formula
        formula = MathTex(
            r"f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left( a_n \cos\left(\frac{2\pi nx}{T}\right) + b_n \sin\left(\frac{2\pi nx}{T}\right) \right)",
            font_size=36
        )
        formula.set_color_by_gradient(YELLOW, ORANGE)
        formula.to_edge(DOWN, buff=0.5)
        
        # Try to load portrait (if available)
        try:
            portrait = SVGMobject("assets/fourier_portrait.svg")
            portrait.scale(1.5)
            portrait.to_edge(RIGHT, buff=1)
            has_portrait = True
        except:
            # Create placeholder circle for portrait
            portrait = Circle(radius=2, color=WHITE, stroke_width=4)
            portrait_text = Text("Portrait", font_size=24)
            portrait_text.move_to(portrait.get_center())
            portrait = VGroup(portrait, portrait_text)
            portrait.to_edge(RIGHT, buff=1)
            has_portrait = False
        
        # Animation sequence
        # 1. Fade in waves from left
        self.play(
            *[FadeIn(wave, shift=RIGHT) for wave in waves],
            run_time=2
        )
        
        # 2. Waves start oscillating
        for wave in waves:
            wave.add_updater(lambda m, dt: m.shift(RIGHT * dt * 0.5))
        
        # 3. Dramatic title appearance
        self.wait(0.5)
        self.play(
            Write(title, run_time=2),
            rate_func=rush_into
        )
        
        # 4. Subtitle fade in
        self.play(FadeIn(subtitle, shift=UP))
        
        # 5. Portrait appears with rotation
        self.wait(0.3)
        if has_portrait:
            self.play(
                FadeIn(portrait, scale=0.5),
                portrait.animate.rotate(2 * PI),
                run_time=2
            )
        else:
            self.play(FadeIn(portrait, shift=LEFT))
        
        # 6. Formula writes in from bottom
        self.wait(0.5)
        self.play(Write(formula), run_time=3)
        
        # 7. Everything pulses together
        self.wait(0.5)
        self.play(
            title.animate.scale(1.1),
            subtitle.animate.scale(1.1),
            portrait.animate.scale(1.1),
            rate_func=there_and_back,
            run_time=1
        )
        
        # 8. Hold the epic moment
        self.wait(2)
        
        # 9. Fade to black dramatically
        self.play(
            *[FadeOut(mob) for mob in [title, subtitle, portrait, formula]],
            *[FadeOut(wave) for wave in waves],
            run_time=2
        )
        
        self.wait(0.5)
    
    def create_fourier_wave(self, frequency=1, amplitude=1, color=BLUE):
        """Create a sine wave representing Fourier series component"""
        wave = FunctionGraph(
            lambda x: amplitude * np.sin(frequency * x),
            x_range=[-2*PI, 2*PI],
            color=color,
            stroke_width=3
        )
        return wave


class WaveCompositionScene(Scene):
    """Bonus scene showing how multiple waves combine (Fourier principle)"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("The Power of Fourier Series", font_size=60)
        title.to_edge(UP)
        title.set_color_by_gradient(BLUE, PURPLE)
        
        # Create individual sine waves
        axes = Axes(
            x_range=[-PI, PI, PI/2],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=3,
            tips=False
        ).scale(0.7)
        
        # Individual components
        wave1 = axes.plot(lambda x: np.sin(x), color=RED)
        label1 = MathTex(r"\sin(x)", color=RED, font_size=36)
        
        wave2 = axes.plot(lambda x: 0.5 * np.sin(3*x), color=GREEN)
        label2 = MathTex(r"\frac{1}{2}\sin(3x)", color=GREEN, font_size=36)
        
        wave3 = axes.plot(lambda x: 0.33 * np.sin(5*x), color=BLUE)
        label3 = MathTex(r"\frac{1}{3}\sin(5x)", color=BLUE, font_size=36)
        
        # Combined wave
        combined = axes.plot(
            lambda x: np.sin(x) + 0.5*np.sin(3*x) + 0.33*np.sin(5*x),
            color=YELLOW,
            stroke_width=4
        )
        label_combined = MathTex(r"\text{Sum}", color=YELLOW, font_size=36)
        
        # Arrange labels
        labels = VGroup(label1, label2, label3, label_combined)
        labels.arrange(RIGHT, buff=0.7)
        labels.to_edge(DOWN, buff=0.5)
        
        # Animations
        self.play(Write(title))
        self.wait(0.5)
        
        # Show individual waves
        self.play(Create(axes))
        self.play(Create(wave1), Write(label1))
        self.wait(0.5)
        
        self.play(Create(wave2), Write(label2))
        self.wait(0.5)
        
        self.play(Create(wave3), Write(label3))
        self.wait(0.5)
        
        # Show combination
        self.play(
            Write(label_combined),
            ReplacementTransform(
                VGroup(wave1.copy(), wave2.copy(), wave3.copy()),
                combined
            ),
            run_time=2
        )
        
        self.wait(2)
        
        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
        
        self.wait(0.5)
