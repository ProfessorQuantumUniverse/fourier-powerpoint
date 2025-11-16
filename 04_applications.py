"""
04_applications.py - Modern Applications of Fourier's Work

Visual demonstrations of how Fourier's theories are used today:
- JPEG compression
- Audio processing (MP3)
- MRI imaging
- Signal processing
- WiFi/Communications
"""

from manim import *
import numpy as np


class ApplicationsIntroScene(Scene):
    """Introduction to modern applications"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Timeline note
        death_note = Text("1830 - Fourier Dies", font_size=48, color=GRAY)
        death_note.to_edge(UP, buff=0.5)
        
        self.play(Write(death_note), run_time=1.5)
        self.wait(1)
        
        # Transition text
        transition = Text(
            "But his legacy lives on...",
            font_size=56,
            color=WHITE,
            slant=ITALIC
        )
        
        self.play(FadeIn(transition, scale=0.8), run_time=1.5)
        self.wait(1.5)
        
        self.play(FadeOut(death_note), FadeOut(transition), run_time=1)
        
        # Modern applications title
        title = Text("Fourier's Modern Legacy", font_size=72, weight=BOLD)
        title.set_color_by_gradient(BLUE, PURPLE, PINK)
        
        self.play(Write(title, run_time=2))
        self.wait(1)
        
        # List of applications with icons/representations
        applications = VGroup(
            Text("📸 Image Compression", font_size=42),
            Text("🎵 Audio Processing", font_size=42),
            Text("🏥 Medical Imaging", font_size=42),
            Text("📡 Communications", font_size=42),
            Text("🔬 Scientific Analysis", font_size=42),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        
        applications.next_to(title, DOWN, buff=1)
        
        # Animate list appearing
        for app in applications:
            app.set_color_by_gradient(BLUE, PURPLE)
            self.play(FadeIn(app, shift=RIGHT), run_time=0.7)
            self.wait(0.3)
        
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)


class JPEGCompressionScene(Scene):
    """Demonstrate JPEG compression using DCT (related to Fourier Transform)"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("JPEG Compression", font_size=64, weight=BOLD)
        title.set_color_by_gradient(BLUE, GREEN)
        title.to_edge(UP, buff=0.3)
        
        subtitle = Text(
            "Using Discrete Cosine Transform (DCT)",
            font_size=32,
            color=GRAY
        )
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(1)
        
        # Simulate image as grid
        grid_size = 8
        
        # Original "image" (checkerboard-like pattern)
        original_grid = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                # Create varying intensities
                intensity = 0.5 + 0.5 * np.sin(i * 0.7) * np.cos(j * 0.7)
                cell = Square(side_length=0.5, stroke_width=1, stroke_color=WHITE)
                cell.set_fill(WHITE, opacity=intensity)
                cell.move_to([i * 0.5 - 2, j * 0.5 - 1.5, 0])
                original_grid.add(cell)
        
        original_label = Text("Original 8×8 Block", font_size=32, color=BLUE)
        original_label.next_to(original_grid, DOWN, buff=0.5)
        
        self.play(FadeOut(title), FadeOut(subtitle))
        self.play(
            FadeIn(original_grid, lag_ratio=0.1),
            Write(original_label),
            run_time=1.5
        )
        self.wait(1)
        
        # Show DCT transformation
        arrow = Arrow(LEFT, RIGHT, color=YELLOW)
        arrow.next_to(original_grid, RIGHT, buff=0.5)
        
        dct_label = Text("DCT", font_size=36, color=YELLOW, weight=BOLD)
        dct_label.next_to(arrow, UP)
        
        self.play(GrowArrow(arrow), Write(dct_label), run_time=1)
        
        # Frequency domain representation (DCT coefficients)
        freq_grid = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                # Low frequencies (top-left) have more energy
                energy = np.exp(-0.3 * (i + j))
                cell = Square(side_length=0.5, stroke_width=1, stroke_color=YELLOW)
                cell.set_fill(YELLOW, opacity=energy)
                cell.move_to([i * 0.5 + 2, j * 0.5 - 1.5, 0])
                freq_grid.add(cell)
        
        freq_label = Text("DCT Coefficients", font_size=32, color=YELLOW)
        freq_label.next_to(freq_grid, DOWN, buff=0.5)
        
        self.play(
            FadeIn(freq_grid, lag_ratio=0.1),
            Write(freq_label),
            run_time=1.5
        )
        self.wait(1)
        
        # Highlight compression opportunity
        compression_note = Text(
            "Most energy in few coefficients!\nDiscard high frequencies = Compression",
            font_size=28,
            color=GREEN,
            line_spacing=1.5
        )
        compression_note.to_edge(DOWN, buff=0.5)
        
        # Highlight top-left corner
        highlight = Square(side_length=2, stroke_width=4, stroke_color=GREEN, fill_opacity=0)
        highlight.move_to([1.25, -0.75, 0])
        
        self.play(
            Create(highlight),
            Write(compression_note),
            run_time=1.5
        )
        self.wait(2)
        
        # Show compression ratio
        ratio = Text("Typical: 10:1 to 20:1 compression!", font_size=36, color=GREEN, weight=BOLD)
        ratio.move_to([0, 2, 0])
        
        self.play(FadeIn(ratio, scale=1.5), run_time=1)
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)


class AudioProcessingScene(Scene):
    """Demonstrate audio processing with Fourier analysis"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("Audio Processing & MP3", font_size=64, weight=BOLD)
        title.set_color_by_gradient(PURPLE, PINK)
        title.to_edge(UP, buff=0.3)
        
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # Audio waveform
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[-1, 1, 0.5],
            x_length=10,
            y_length=3,
            axis_config={"color": GRAY}
        ).shift(UP * 1)
        
        # Complex audio signal
        audio_wave = axes.plot(
            lambda t: 0.5*np.sin(2*PI*2*t) + 0.3*np.sin(2*PI*5*t) + 0.2*np.sin(2*PI*8*t) + 0.1*np.sin(2*PI*12*t),
            color=PURPLE,
            stroke_width=3
        )
        
        wave_label = Text("Audio Signal (Time)", font_size=32, color=PURPLE)
        wave_label.next_to(axes, DOWN, buff=0.3)
        
        self.play(FadeOut(title))
        self.play(Create(axes))
        self.play(Create(audio_wave, run_time=2), Write(wave_label))
        self.wait(1)
        
        # Show FFT transformation
        self.play(
            axes.animate.shift(LEFT * 3),
            audio_wave.animate.shift(LEFT * 3),
            wave_label.animate.shift(LEFT * 3),
            run_time=1
        )
        
        # Frequency spectrum
        freq_axes = Axes(
            x_range=[0, 15, 5],
            y_range=[0, 1, 0.5],
            x_length=5,
            y_length=3,
            axis_config={"color": GRAY}
        ).shift(RIGHT * 3 + UP * 1)
        
        # Frequency peaks
        frequencies = [2, 5, 8, 12]
        amplitudes = [0.5, 0.3, 0.2, 0.1]
        
        freq_peaks = VGroup()
        for freq, amp in zip(frequencies, amplitudes):
            peak = freq_axes.plot_line_graph(
                x_values=[freq, freq],
                y_values=[0, amp],
                add_vertex_dots=False,
                line_color=PINK,
                stroke_width=6
            )
            freq_peaks.add(peak)
        
        freq_label = Text("Frequency Spectrum", font_size=32, color=PINK)
        freq_label.next_to(freq_axes, DOWN, buff=0.3)
        
        # Arrow
        arrow = Arrow(
            axes.get_right() + RIGHT * 0.3,
            freq_axes.get_left() + LEFT * 0.3,
            color=YELLOW
        )
        arrow_label = Text("FFT", font_size=28, color=YELLOW, weight=BOLD)
        arrow_label.next_to(arrow, UP)
        
        self.play(Create(freq_axes))
        self.play(GrowArrow(arrow), Write(arrow_label))
        self.play(*[Create(peak) for peak in freq_peaks], Write(freq_label), run_time=1.5)
        self.wait(1)
        
        # Show compression concept
        self.play(
            *[FadeOut(mob) for mob in [axes, audio_wave, wave_label, arrow, arrow_label]],
            freq_axes.animate.move_to([0, 1, 0]),
            freq_peaks.animate.move_to([0, 1, 0]),
            freq_label.animate.next_to([0, 1, 0], DOWN, buff=2),
            run_time=1.5
        )
        
        # Explain MP3 compression
        explanation = VGroup(
            Text("MP3 Compression Strategy:", font_size=36, color=YELLOW, weight=BOLD),
            Text("• Remove inaudible frequencies", font_size=28),
            Text("• Compress less important data", font_size=28),
            Text("• Result: ~90% size reduction!", font_size=28, color=GREEN),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        explanation.to_edge(DOWN, buff=0.5)
        
        for line in explanation:
            self.play(FadeIn(line, shift=UP), run_time=0.7)
            self.wait(0.3)
        
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)


class MRIScene(Scene):
    """Demonstrate MRI imaging using Fourier transforms"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("Medical Imaging (MRI)", font_size=64, weight=BOLD)
        title.set_color_by_gradient(BLUE, TEAL, GREEN)
        title.to_edge(UP, buff=0.3)
        
        subtitle = Text(
            "Magnetic Resonance Imaging relies on Fourier Transforms",
            font_size=28,
            color=GRAY
        )
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(1)
        
        # Show k-space (frequency domain data)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        kspace_label = Text("K-Space Data", font_size=42, color=TEAL)
        kspace_label.to_edge(LEFT).shift(UP * 2)
        
        # Simulate k-space as grid with center bright
        kspace = VGroup()
        grid_size = 20
        for i in range(grid_size):
            for j in range(grid_size):
                x = (i - grid_size/2) / (grid_size/2)
                y = (j - grid_size/2) / (grid_size/2)
                distance = np.sqrt(x**2 + y**2)
                intensity = np.exp(-distance * 2)
                
                cell = Square(side_length=0.25, stroke_width=0)
                cell.set_fill(TEAL, opacity=intensity)
                cell.move_to([i * 0.25 - 2.5, j * 0.25, 0]).shift(LEFT * 3)
                kspace.add(cell)
        
        self.play(Write(kspace_label))
        self.play(FadeIn(kspace, lag_ratio=0.05), run_time=2)
        self.wait(1)
        
        # Show inverse Fourier transform
        arrow = Arrow(LEFT, RIGHT, color=YELLOW, stroke_width=6)
        arrow.scale(1.5)
        
        ift_label = Text("Inverse\nFourier\nTransform", font_size=28, color=YELLOW, line_spacing=1.2)
        ift_label.next_to(arrow, UP)
        
        self.play(GrowArrow(arrow), Write(ift_label), run_time=1.5)
        
        # Show resulting image
        image_label = Text("MRI Image", font_size=42, color=GREEN)
        image_label.to_edge(RIGHT).shift(UP * 2)
        
        # Simulate brain scan (simple representation)
        brain_image = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                x = (i - grid_size/2) / (grid_size/2)
                y = (j - grid_size/2) / (grid_size/2)
                distance = np.sqrt(x**2 + y**2)
                
                # Create brain-like structure
                if distance < 0.9:
                    intensity = 0.5 + 0.5 * np.sin(i * 0.5) * np.cos(j * 0.5)
                    intensity *= np.exp(-distance * 0.5)
                else:
                    intensity = 0
                
                cell = Square(side_length=0.25, stroke_width=0)
                cell.set_fill(GREEN, opacity=intensity)
                cell.move_to([i * 0.25 - 2.5, j * 0.25, 0]).shift(RIGHT * 3)
                brain_image.add(cell)
        
        self.play(Write(image_label))
        self.play(FadeIn(brain_image, lag_ratio=0.05), run_time=2)
        self.wait(2)
        
        # Impact text
        impact = Text(
            "Fourier transforms save lives every day!",
            font_size=40,
            color=YELLOW,
            weight=BOLD
        )
        impact.to_edge(DOWN, buff=0.5)
        
        self.play(Write(impact, run_time=2))
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)


class SignalProcessingScene(Scene):
    """Show WiFi and communications applications"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("Wireless Communications", font_size=64, weight=BOLD)
        title.set_color_by_gradient(BLUE, PURPLE, PINK)
        title.to_edge(UP, buff=0.3)
        
        subtitle = Text("WiFi, 5G, Radio - All Use Fourier Analysis", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(1)
        
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Show multiple signals sharing spectrum
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 1, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": GRAY},
            tips=False
        )
        
        axes_label = Text("Frequency Spectrum", font_size=36, color=WHITE)
        axes_label.next_to(axes, DOWN, buff=0.5)
        
        self.play(Create(axes), Write(axes_label))
        
        # Different frequency channels
        channels = [
            (1, 0.8, "WiFi Ch 1", RED),
            (3, 0.7, "WiFi Ch 6", GREEN),
            (5, 0.9, "WiFi Ch 11", BLUE),
            (7, 0.6, "Bluetooth", YELLOW),
            (9, 0.75, "5G", PURPLE),
        ]
        
        channel_bars = VGroup()
        labels = VGroup()
        
        for freq, amp, name, color in channels:
            bar = axes.plot_line_graph(
                x_values=[freq, freq],
                y_values=[0, amp],
                add_vertex_dots=False,
                line_color=color,
                stroke_width=8
            )
            channel_bars.add(bar)
            
            label = Text(name, font_size=20, color=color)
            label.next_to([axes.c2p(freq, amp)[0], axes.c2p(freq, amp)[1], 0], UP, buff=0.1)
            labels.add(label)
        
        # Animate channels appearing
        for bar, label in zip(channel_bars, labels):
            self.play(Create(bar), Write(label), run_time=0.8)
            self.wait(0.2)
        
        self.wait(1)
        
        # Explanation
        explanation = Text(
            "Fourier analysis separates overlapping signals",
            font_size=36,
            color=YELLOW
        )
        explanation.to_edge(UP, buff=0.5)
        
        self.play(Write(explanation), run_time=1.5)
        self.wait(2)
        
        # Show OFDM concept
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
        
        ofdm_title = Text("OFDM: Modern WiFi/5G", font_size=56, weight=BOLD)
        ofdm_title.set_color_by_gradient(BLUE, PURPLE)
        ofdm_title.to_edge(UP, buff=0.5)
        
        ofdm_subtitle = Text(
            "Orthogonal Frequency Division Multiplexing",
            font_size=28,
            color=GRAY
        )
        ofdm_subtitle.next_to(ofdm_title, DOWN, buff=0.2)
        
        self.play(Write(ofdm_title), FadeIn(ofdm_subtitle, shift=UP))
        self.wait(1)
        
        # Show multiple orthogonal sine waves
        ofdm_axes = Axes(
            x_range=[0, 2*PI, PI],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            y_length=4,
            axis_config={"color": GRAY},
            tips=False
        ).shift(DOWN * 0.5)
        
        self.play(Create(ofdm_axes))
        
        # Multiple orthogonal carriers
        carriers = VGroup()
        for i in range(1, 6):
            carrier = ofdm_axes.plot(
                lambda x, n=i: 0.4 * np.sin(n * x),
                color=interpolate_color(BLUE, RED, i/6),
                stroke_width=2
            )
            carriers.add(carrier)
        
        self.play(*[Create(c) for c in carriers], run_time=2, lag_ratio=0.2)
        self.wait(1)
        
        result_text = Text(
            "Each carrier transmits data independently!",
            font_size=32,
            color=GREEN
        )
        result_text.to_edge(DOWN, buff=0.5)
        
        self.play(Write(result_text))
        self.wait(2)
        
        # Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)
