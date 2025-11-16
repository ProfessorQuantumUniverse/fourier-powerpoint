"""
02_timeline.py - Timeline Animation for Fourier's Life During French Revolution

This scene creates an elegant timeline moving from point to point,
leaving space above for images and additional content.
"""

from manim import *


class TimelineScene(Scene):
    """Interactive timeline of Fourier's life during the French Revolution"""
    
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        
        # Title
        title = Text("Joseph Fourier: Life & Times", font_size=56, weight=BOLD)
        title.set_color_by_gradient(BLUE, PURPLE)
        title.to_edge(UP, buff=0.3)
        
        # Timeline data (year, event, color)
        events = [
            (1768, "Born in Auxerre, France", BLUE),
            (1789, "French Revolution Begins", RED),
            (1794, "Arrested During Terror", DARK_RED),
            (1795, "Released, Begins Teaching", GREEN),
            (1798, "Joins Napoleon's Egypt Expedition", GOLD),
            (1801, "Returns to France, Prefect of Isère", ORANGE),
            (1807, "Submits Heat Theory Paper", YELLOW),
            (1822, "Publishes Analytical Theory of Heat", PURPLE),
            (1830, "Dies in Paris", GRAY),
        ]
        
        # Create timeline base line
        timeline_y = -1.5
        timeline_start_x = -6
        timeline_end_x = 6
        timeline_length = timeline_end_x - timeline_start_x
        
        timeline_line = Line(
            start=[timeline_start_x, timeline_y, 0],
            end=[timeline_end_x, timeline_y, 0],
            stroke_width=4,
            color=WHITE
        )
        
        # Create timeline markers and labels
        timeline_markers = VGroup()
        event_labels = VGroup()
        year_labels = VGroup()
        
        num_events = len(events)
        for i, (year, event, color) in enumerate(events):
            # Calculate position along timeline
            x_pos = timeline_start_x + (i / (num_events - 1)) * timeline_length
            
            # Create marker point
            marker = Dot(
                point=[x_pos, timeline_y, 0],
                radius=0.12,
                color=color,
                fill_opacity=1
            )
            marker.set_z_index(2)
            
            # Create glow effect
            glow = Circle(
                radius=0.2,
                color=color,
                fill_opacity=0,
                stroke_width=2,
                stroke_opacity=0.5
            )
            glow.move_to(marker.get_center())
            marker.add(glow)
            
            timeline_markers.add(marker)
            
            # Year label (below timeline)
            year_label = Text(str(year), font_size=28, color=color, weight=BOLD)
            year_label.next_to(marker, DOWN, buff=0.3)
            year_labels.add(year_label)
            
            # Event description (above timeline)
            event_label = Text(event, font_size=24, color=WHITE)
            event_label.next_to(marker, UP, buff=0.4)
            event_label.set_max_width(2.5)
            event_labels.add(event_label)
        
        # Create animated indicator that moves along timeline
        indicator = Triangle(color=YELLOW, fill_opacity=1)
        indicator.scale(0.2)
        indicator.rotate(-PI/2)
        indicator.next_to(timeline_markers[0], UP, buff=0.05)
        
        # Animation sequence
        # 1. Show title
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # 2. Draw timeline
        self.play(Create(timeline_line), run_time=2)
        self.wait(0.3)
        
        # 3. Animate through each event
        for i, (marker, year_label, event_label) in enumerate(zip(
            timeline_markers, year_labels, event_labels
        )):
            if i == 0:
                # First event - show everything
                self.play(
                    FadeIn(marker, scale=0.5),
                    FadeIn(indicator),
                    run_time=0.5
                )
                self.play(Write(year_label), run_time=0.5)
                self.play(FadeIn(event_label, shift=DOWN), run_time=0.7)
                self.wait(1)
            else:
                # Move indicator to next event
                self.play(
                    indicator.animate.next_to(marker, UP, buff=0.05),
                    FadeIn(marker, scale=0.5),
                    run_time=1
                )
                
                # Show year and event
                self.play(Write(year_label), run_time=0.5)
                self.play(FadeIn(event_label, shift=DOWN), run_time=0.7)
                
                # Pulse the current marker
                self.play(
                    marker.animate.scale(1.3),
                    rate_func=there_and_back,
                    run_time=0.5
                )
                
                self.wait(0.8)
        
        # 4. Hold final frame
        self.wait(2)
        
        # 5. Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
        
        self.wait(0.5)


class DetailedTimelineScene(Scene):
    """Alternative timeline with more visual details"""
    
    def construct(self):
        self.camera.background_color = "#0a0a0a"
        
        # Title
        title = Text("The Revolutionary Era", font_size=64)
        title.set_color_by_gradient(RED, BLUE, WHITE)
        title.to_edge(UP, buff=0.4)
        
        # Subtitle
        subtitle = Text("Fourier's Journey Through History", font_size=36, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        # Timeline setup
        timeline_y = 0
        timeline_start_x = -5.5
        timeline_end_x = 5.5
        
        # Main timeline
        timeline = Line(
            start=[timeline_start_x, timeline_y, 0],
            end=[timeline_end_x, timeline_y, 0],
            stroke_width=6,
            color=WHITE
        )
        timeline.set_color_by_gradient(BLUE, RED, PURPLE)
        
        # Key periods
        periods = [
            ("Youth", 1768, 1789, BLUE, -5.5, -2.5),
            ("Revolution", 1789, 1799, RED, -2.5, 0),
            ("Napoleon", 1799, 1815, GOLD, 0, 2.5),
            ("Restoration", 1815, 1830, PURPLE, 2.5, 5.5),
        ]
        
        period_boxes = VGroup()
        period_labels = VGroup()
        
        for name, start_year, end_year, color, x_start, x_end in periods:
            # Period indicator box
            box = Rectangle(
                width=x_end - x_start,
                height=0.5,
                fill_opacity=0.2,
                fill_color=color,
                stroke_width=2,
                stroke_color=color
            )
            box_center_x = (x_start + x_end) / 2
            box.move_to([box_center_x, timeline_y - 1.5, 0])
            period_boxes.add(box)
            
            # Period label
            label = VGroup(
                Text(name, font_size=32, weight=BOLD, color=color),
                Text(f"{start_year}-{end_year}", font_size=20, color=GRAY)
            ).arrange(DOWN, buff=0.1)
            label.move_to(box.get_center())
            period_labels.add(label)
        
        # Animations
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(0.5)
        
        self.play(Create(timeline), run_time=2.5)
        self.wait(0.5)
        
        # Reveal periods one by one
        for box, label in zip(period_boxes, period_labels):
            self.play(
                FadeIn(box, scale=0.8),
                Write(label),
                run_time=1.2
            )
            self.wait(0.6)
        
        self.wait(2)
        
        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
        
        self.wait(0.5)


class TimelineWithPortraitsScene(Scene):
    """Timeline with space for portrait integration"""
    
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        
        # Simple clean timeline at bottom
        timeline_y = -2.5
        
        # Timeline elements
        line = Line(
            start=[-6, timeline_y, 0],
            end=[6, timeline_y, 0],
            stroke_width=4,
            color=BLUE_D
        )
        
        # Major life events
        milestones = [
            (-4, "1768\nBirth", BLUE),
            (-2, "1789\nRevolution", RED),
            (0, "1807\nHeat Theory", YELLOW),
            (2, "1822\nMajor Work", ORANGE),
            (4, "1830\nDeath", PURPLE),
        ]
        
        points = VGroup()
        labels = VGroup()
        
        for x, text, color in milestones:
            point = Dot([x, timeline_y, 0], radius=0.15, color=color)
            points.add(point)
            
            label = Text(text, font_size=24, color=color).next_to(point, DOWN, buff=0.3)
            labels.add(label)
        
        # Note for user
        note = Text(
            "Space above reserved for images and additional content",
            font_size=28,
            color=GRAY,
            slant=ITALIC
        )
        note.move_to([0, 1.5, 0])
        
        # Animate
        self.play(Create(line), run_time=2)
        self.play(*[GrowFromCenter(p) for p in points], run_time=1.5)
        self.play(*[Write(l) for l in labels], run_time=2)
        self.wait(1)
        
        self.play(FadeIn(note, shift=DOWN), run_time=1)
        self.wait(2)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=1.5)
        self.wait(0.5)
