from manim import *
import numpy as np
from manim.utils.color.X11 import LIGHTBLUE

DEFAULT_FONT = "Latin Modern Roman 12"
class IntroScene(Scene):
    def construct(self):
        logo = ImageMobject("logo-hcmus-new.png")
        logo.scale(0.4).to_edge(UP)

        school_name = Text(
            "Trường Đại học Khoa học Tự nhiên - ĐHQG-HCM",
            font_size=32,
            font=DEFAULT_FONT
        )

        class_name = Text(
            "Lớp 24CTT3",
            font_size=30,
            font=DEFAULT_FONT
        )

        subject = Text(
            "Toán Ứng Dụng & Thống Kê",
            font_size=36,
            color=BLUE,
            font=DEFAULT_FONT
        )

        info_group = VGroup(
            school_name,
            class_name,
            subject
        ).arrange(DOWN, buff=0.7)

        info_group.next_to(logo, DOWN)

        self.play(
            FadeIn(logo),
            Write(info_group)
        )
        self.wait(2)

        # ======================
        # FRAME 2: Thành viên (FIX ALIGN)
        # ======================
        group_title = Text(
            "NHÓM 2",
            font_size=40,
            color=YELLOW,
            font=DEFAULT_FONT
        ).to_edge(UP)
        ids = [
            "24120381",
            "24120288",
            "24120276",
            "24120300",
            "24120369"
        ]

        names = [
            "Ngô Hoàng Minh",
            "Nguyễn Thành Dự",
            "Mai Thúc Hải Đăng",
            "Đỗ Ngọc Hải",
            "Nguyễn Xuân Lộc"
        ]

        # 👉 Tạo từng dòng (row)
        rows = VGroup()
        for i in range(len(ids)):
            id_text = Text(ids[i], font_size=28, font=DEFAULT_FONT)
            name_text = Text(names[i], font_size=28, font=DEFAULT_FONT)

            row = VGroup(id_text, name_text).arrange(RIGHT, buff=1.5)
            rows.add(row)

        # 👉 Căn toàn bộ theo LEFT để thẳng hàng
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        rows.next_to(group_title, DOWN, buff=0.7)

        self.play(
            FadeOut(logo),
            FadeOut(info_group),
            Write(group_title)
        )

        # Animation từng dòng
        self.play(
            LaggedStart(*[FadeIn(row, shift=RIGHT) for row in rows], lag_ratio=0.2)
        )

        self.wait(2)
class Scene1(Scene):

    """IN RA LỜI CHÀO"""
    def construct(self):
        text1 = Text("Linear Algebra", color=YELLOW).scale(0.9).to_edge(UP)
        text2 = Text("Phân rã SVD", weight=BOLD, color=RED_A).scale(1.2)

        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-2.5, 2.5, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.4
            }
        )

        self.play(Write(text1), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(plane), run_time=1)
        self.play(FadeIn(text2, shift=UP), run_time=1.2)
        box = SurroundingRectangle(text2, color=RED, buff=0.2)
        self.play(Create(box))
        self.wait(5)

class Scene2(Scene):
    def construct(self):
        title = Text("Phân rã SVD là gì ?", color=YELLOW).to_edge(UP)

        desc = Text(
            "Mọi ma trận A (m×n), hạng r đều có thể phân rã thành tích của 3 ma trận",
            font_size=30,
            font="Latin Modern Roman 12"
        ).next_to(title, DOWN, buff=0.5)

        formula = MathTex(r"A = U \Sigma V^{T}")
        formula.next_to(desc, DOWN, buff=0.8)

        explain_U = VGroup(
            MathTex("U:"),
            Text(" ma trận trực giao (m × m)", font=DEFAULT_FONT, font_size=28)
        ).arrange(RIGHT)

        explain_S = VGroup(
            MathTex(r"\Sigma:"),
            Text(" ma trận đường chéo (m × n)", font=DEFAULT_FONT, font_size=28)
        ).arrange(RIGHT)

        explain_V = VGroup(
            MathTex(r"V^T:"),
            Text(" chuyển vị của ma trận trực giao (n × n)", font=DEFAULT_FONT, font_size=28)
        ).arrange(RIGHT)

        explain_group = VGroup(explain_U, explain_S, explain_V)\
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)\
            .next_to(formula, DOWN, buff=0.8)

        self.play(Write(title))
        self.play(FadeIn(desc, shift=UP))
        self.play(Write(formula))
        box = SurroundingRectangle(formula, color=RED, buff=0.2)
        self.play(Create(box))
        self.play(Indicate(formula[0][2]))
        self.play(Write(explain_U))

        self.play(Indicate(formula[0][3]))
        self.play(Write(explain_S))

        self.play(Indicate(formula[0][4:]))
        self.play(Write(explain_V))

        self.wait(2)


class Scene3(Scene):
    """Tìm hiểu về ma trận trực giao"""

    def construct(self) -> None:
        # ===== TIÊU ĐỀ =====
        title = Text("Ma trận trực giao là gì?", font=DEFAULT_FONT, color=YELLOW) \
            .scale(0.8) \
            .to_edge(UP)

        definition = Text("Ma trận Q trực giao nếu:", font=DEFAULT_FONT, font_size=28)
        formula = MathTex(r"Q^T Q = I")

        q_def = MathTex(r"Q = \begin{pmatrix} v_1 & v_2 \end{pmatrix}").scale(0.8)
        dot_matrix = MathTex(
            r"\begin{pmatrix} v_1 \cdot v_1 & v_1 \cdot v_2 \\ v_2 \cdot v_1 & v_2 \cdot v_2 \end{pmatrix}",
            "=",
            r"\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}"
        ).scale(0.7)

        conclusion1 = MathTex(r"\Rightarrow ||v_1|| = ||v_2|| = 1", color=YELLOW).scale(0.8)
        conclusion2 = MathTex(r"\Rightarrow v_1 \perp v_2", color=YELLOW).scale(0.8)

        left_group = VGroup(
            definition,
            formula,
            q_def,
            dot_matrix,
            conclusion1,
            conclusion2
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT, buff=0.8)
        formula.set_x(left_group.get_center()[0])
        box = SurroundingRectangle(formula, color=RED, buff=0.2)

        plane = NumberPlane(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            x_length=4.5,
            y_length=4.5,
            background_line_style={"stroke_opacity": 0.4}
        )

        v1 = plane.get_vector([1, 0], color=BLUE)
        v2 = plane.get_vector([0, 1], color=GREEN)
        right_angle = RightAngle(v1, v2, length=0.25)

        label_v1 = MathTex("v_1").scale(0.7).next_to(v1.get_end(), DOWN)
        label_v2 = MathTex("v_2").scale(0.7).next_to(v2.get_end(), LEFT)

        right_group = VGroup(plane, v1, v2, right_angle, label_v1, label_v2) \
            .to_edge(RIGHT, buff=0.8) \
            .shift(DOWN * 0.5)

        divider = Line(UP * 2.5, DOWN * 2.5, color=GRAY).move_to(ORIGIN)

        self.play(Write(title))

        self.play(Write(definition))
        self.play(Write(formula))
        self.play(Create(box))

        self.wait(0.5)

        self.play(Write(q_def))
        self.play(Write(dot_matrix))
        self.play(Write(conclusion1))
        self.play(Write(conclusion2))

        self.play(Create(divider))
        self.play(FadeIn(plane))

        self.play(GrowArrow(v1), Write(label_v1))
        self.play(GrowArrow(v2), Write(label_v2))
        self.play(Create(right_angle))

        self.wait(1)

        rot_angle = -PI / 3
        center_pt = plane.get_center()

        self.play(
            Rotate(v1, angle=rot_angle, about_point=center_pt),
            Rotate(v2, angle=rot_angle, about_point=center_pt),
            Rotate(label_v1, angle=rot_angle, about_point=center_pt),
            Rotate(label_v2, angle=rot_angle, about_point=center_pt),
            Rotate(right_angle, angle=rot_angle, about_point=center_pt),
            run_time=2
        )

        self.wait(2)


class Scene4(Scene):
    def construct(self) -> None:
        title = Text("Ý nghĩa hình học", font=DEFAULT_FONT, color=YELLOW).to_edge(UP)
        formula = MathTex(r"A = U \Sigma V^T").scale(1.2).next_to(title, DOWN, buff=0.5)

        step1 = Text("1. Quay", font=DEFAULT_FONT).scale(0.6)
        step2 = Text("2. Co giãn", font=DEFAULT_FONT).scale(0.6)
        step3 = Text("3. Quay", font=DEFAULT_FONT).scale(0.6)

        v_t = MathTex("V^T")
        sigma = MathTex(r"\Sigma")
        u = MathTex("U")

        g1 = VGroup(v_t, step1).arrange(DOWN)
        g2 = VGroup(sigma, step2).arrange(DOWN)
        g3 = VGroup(u, step3).arrange(DOWN)

        steps = VGroup(g1, g2, g3).arrange(RIGHT, buff=1.5).next_to(formula, DOWN, buff=0.5)
        arr1 = Arrow(g1.get_right(), g2.get_left(), buff=0.2)
        arr2 = Arrow(g2.get_right(), g3.get_left(), buff=0.2)

        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(0.6).to_edge(DOWN, buff=0.5)

        center_pt = plane.get_center()
        circle = Circle(radius=0.6, color=WHITE).move_to(center_pt)
        v1 = plane.get_vector([1, 0], color=BLUE)
        v2 = plane.get_vector([0, 1], color=GREEN)

        visuals = VGroup(plane, circle, v1, v2)

        self.play(Write(title))
        self.play(Write(formula))
        self.play(FadeIn(steps), GrowArrow(arr1), GrowArrow(arr2))
        self.play(FadeIn(visuals))
        self.wait(0.5)

        self.play(Indicate(g1, color=RED))
        self.play(
            Rotate(circle, angle=-PI/4, about_point=center_pt),
            Rotate(v1, angle=-PI/4, about_point=center_pt),
            Rotate(v2, angle=-PI/4, about_point=center_pt),
            run_time=1.5
        )

        self.play(Indicate(g2, color=RED))
        self.play(
            circle.animate.stretch(2, dim=0, about_point=center_pt).stretch(0.5, dim=1, about_point=center_pt),
            v1.animate.stretch(2, dim=0, about_point=center_pt).stretch(0.5, dim=1, about_point=center_pt),
            v2.animate.stretch(2, dim=0, about_point=center_pt).stretch(0.5, dim=1, about_point=center_pt),
            run_time=1.5
        )

        self.play(Indicate(g3, color=RED))
        self.play(
            Rotate(circle, angle=PI/3, about_point=center_pt),
            Rotate(v1, angle=PI/3, about_point=center_pt),
            Rotate(v2, angle=PI/3, about_point=center_pt),
            run_time=1.5
        )

        self.wait(2)


class Scene5(Scene):
    def construct(self) -> None:

        title = Text("Các bước phân rã SVD", font=DEFAULT_FONT, color=YELLOW) \
            .to_edge(UP)

        step1_text = Text(
            "Bước 1: Tính ma trận tích và tìm trị riêng, vector riêng",
            font=DEFAULT_FONT,
            font_size=32
        ).next_to(title, DOWN, buff=0.5)

        ata = MathTex("A^T A").scale(1.5)

        det_eq = MathTex(r"\det(A^T A - \lambda I) = 0").scale(1.2)

        lamda_res = MathTex(r"\lambda_1 \ge \lambda_2 \ge \dots \ge 0", color=ORANGE)
        lamda_label = Text("Trị riêng", font=DEFAULT_FONT, font_size=24).next_to(lamda_res, LEFT, buff=0.5)

        vec_res = MathTex(r"v_1, v_2, \dots", color=GREEN)
        vec_label = Text("Vector riêng trực chuẩn", font=DEFAULT_FONT, font_size=24).next_to(vec_res, LEFT, buff=0.5)

        res_lamda_group = VGroup(lamda_label, lamda_res)
        res_vec_group = VGroup(vec_label, vec_res)

        result_group = VGroup(res_lamda_group, res_vec_group) \
            .arrange(DOWN, aligned_edge=RIGHT, buff=0.5)

        flowchart = VGroup(ata, det_eq, result_group) \
            .arrange(DOWN, buff=1.0) \
            .next_to(step1_text, DOWN, buff=0.8)

        arrow1 = Arrow(ata.get_bottom(), det_eq.get_top(), buff=0.2)
        arrow2 = Arrow(det_eq.get_bottom(), result_group.get_top(), buff=0.2)

        box = SurroundingRectangle(ata, color=RED, buff=0.2)
        box2 = SurroundingRectangle(det_eq, color=GREEN, buff=0.2)
        self.play(Write(title))
        self.play(FadeIn(step1_text, shift=DOWN))
        self.wait(0.5)

        self.play(Write(ata))
        self.play(Create(box))
        self.wait(0.5)

        self.play(GrowArrow(arrow1))
        self.play(Write(det_eq))
        self.play(Create(box2))
        self.wait(0.5)

        self.play(GrowArrow(arrow2))
        self.play(FadeIn(result_group, shift=UP))

        self.wait(2)


class Scene6(Scene):
    def construct(self) -> None:

        title = Text("Bước 2: Thiết lập ma trận Σ và V", font=DEFAULT_FONT) \
            .to_edge(UP)

        desc_sigma = Text("1. Tính giá trị suy biến", font=DEFAULT_FONT, font_size=28, color=BLUE)

        lamda_sort = MathTex(r"\lambda_1 \ge \lambda_2 \ge \dots \ge 0").scale(0.8)
        calc_sigma = MathTex(r"\sigma_i = \sqrt{\lambda_i}").scale(0.8)
        sigma_matrix = MathTex(
            r"\Sigma = \begin{pmatrix} \sigma_1 & 0 & \cdots \\ 0 & \sigma_2 & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}"
        ).scale(0.9)

        group_sigma = VGroup(desc_sigma, lamda_sort, calc_sigma, sigma_matrix) \
            .arrange(DOWN, buff=0.6)

        arr_s1 = Arrow(lamda_sort.get_bottom(), calc_sigma.get_top(), buff=0.15)
        arr_s2 = Arrow(calc_sigma.get_bottom(), sigma_matrix.get_top(), buff=0.15)

        left_part = VGroup(group_sigma, arr_s1, arr_s2).to_edge(LEFT, buff=1.0)

        desc_v = Text("2. Lập ma trận trực giao V", font=DEFAULT_FONT, font_size=28, color=GREEN)

        v_vecs = MathTex(r"v_1, v_2, \dots \text{ (vector riêng)}").scale(0.8)
        v_matrix = MathTex(
            r"V = \begin{pmatrix} | & | & \\ v_1 & v_2 & \cdots \\ | & | & \end{pmatrix}"
        ).scale(0.9)

        group_v = VGroup(desc_v, v_vecs, v_matrix) \
            .arrange(DOWN, buff=0.8)

        arr_v = Arrow(v_vecs.get_bottom(), v_matrix.get_top(), buff=0.15)

        right_part = VGroup(group_v, arr_v).to_edge(RIGHT, buff=1.5)

        right_part.align_to(left_part, UP)

        VGroup(left_part, right_part).next_to(title, DOWN, buff=0.5)

        divider = Line(UP * 2.5, DOWN * 2.5, color=GRAY)

        self.play(Write(title))
        self.wait(2)

        self.play(Write(desc_sigma))
        self.wait(1.1)

        self.play(FadeIn(lamda_sort, shift=DOWN))
        self.wait(3.0)

        self.play(GrowArrow(arr_s1), Write(calc_sigma))
        self.wait(2.5)
        self.play(GrowArrow(arr_s2), Write(sigma_matrix))
        self.wait(4.0)

        self.play(Create(divider))
        self.wait(1.0)

        self.play(Write(desc_v))
        self.wait(2.0)

        self.play(FadeIn(v_vecs, shift=DOWN))
        self.wait(3.5)

        self.play(GrowArrow(arr_v), Write(v_matrix))
        self.wait(3.5)

        self.wait(2.0)


class Scene7(Scene):
    def construct(self) -> None:

        title = Text("Bước 3: Thiết lập ma trận U", font=DEFAULT_FONT).scale(0.8).to_edge(UP)

        step1_text = Text(
            "1. Tính các cột của U\n(từ trị suy biến khác 0):",
            font=DEFAULT_FONT, font_size=26, color=BLUE
        )
        formula_u = MathTex(r"u_i = \frac{1}{\sigma_i} A v_i").scale(0.9)

        left_col = VGroup(step1_text, formula_u).arrange(DOWN, buff=0.4)
        left_col.next_to(title, DOWN, buff=0.8).to_edge(LEFT, buff=0.8)

        step2_text = Text(
            "2. Trường hợp r < m:",
            font=DEFAULT_FONT, font_size=26, color=GREEN
        )

        explain_part1 = Text(
            "Mở rộng hệ trực chuẩn trong",
            font=DEFAULT_FONT,
            font_size=24
        )
        math_rm = MathTex(r"\mathbb{R}^m")

        explain_group = VGroup(explain_part1, math_rm).arrange(RIGHT, buff=0.2)

        matrix_u = MathTex(
            r"U = \begin{pmatrix} | & | & & | \\ u_1 & u_2 & \cdots & u_m \\ | & | & & | \end{pmatrix}"
        ).scale(0.8)

        right_col = VGroup(step2_text, explain_group, matrix_u).arrange(DOWN, buff=0.4)
        right_col.next_to(title, DOWN, buff=0.8).to_edge(RIGHT, buff=0.8)

        box = SurroundingRectangle(formula_u, color=YELLOW, buff=0.2)

        self.play(Write(title))

        self.play(Write(step1_text))
        self.play(FadeIn(formula_u, shift=UP))
        self.play(Create(box))

        self.play(Write(step2_text))
        self.play(FadeIn(explain_group, shift=UP))

        self.play(Write(matrix_u))

        self.wait(2)

class Scene8(Scene):
    def construct(self) -> None:

        title_word = Text("Ví dụ: ", font=DEFAULT_FONT, color=YELLOW)
        title_text = Text("Thực hiện phân rã SVD cho ", font=DEFAULT_FONT, color=WHITE)
        title_math = MathTex(r"A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}")

        title_group = VGroup(title_word, title_text, title_math).arrange(RIGHT).to_edge(UP)

        step1_title = Text("Bước 1: Tính các trị riêng của ", font=DEFAULT_FONT, color = BLUE).scale(0.8)
        step1_math = MathTex("A^TA").scale(0.8).next_to(step1_title, RIGHT)
        # Giảm buff để đẩy toàn bộ nội dung lên cao hơn
        step1_group = VGroup(step1_title, step1_math).next_to(title_group, DOWN, buff=0.4).to_edge(LEFT, buff=1)

        ata_calc = MathTex(
            r"A^T A = \begin{pmatrix} 1 & 0 \\ 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}"
        ).scale(0.8)

        det_calc = MathTex(
            r"\det(A^T A - \lambda I) = \det \begin{pmatrix} 1-\lambda & 1 & 0 \\ 1 & 1-\lambda & 0 \\ 0 & 0 & 1-\lambda \end{pmatrix} = 0"
        ).scale(0.8)

        lamda_res = MathTex(
            r"\Rightarrow \lambda_1 = 2, \lambda_2 = 1, \lambda_3 = 0", color=GREEN
        ).scale(0.9)

        math_group = VGroup(ata_calc, det_calc, lamda_res).arrange(DOWN, buff=0.3).next_to(step1_group, DOWN, buff=0.4).align_to(RIGHT)
        math_group.set_x(0)
        box = SurroundingRectangle(lamda_res,color = ORANGE, buff = 0.2)
        self.play(Write(title_group))
        self.wait(2)

        self.play(Write(step1_group))
        self.wait(1)

        self.play(FadeIn(ata_calc, shift=UP))
        self.wait(2)

        self.play(FadeIn(det_calc, shift=UP))
        self.wait(2)

        self.play(Write(lamda_res))
        self.play(Create(box))
        self.wait(2)


class Scene9(Scene):
    def construct(self) -> None:
        step1_cont = Text("Bước 1 (tiếp): Tìm các vector riêng trực chuẩn", font=DEFAULT_FONT, color=BLUE) \
            .scale(0.8) \
            .to_edge(UP, buff=0.5)

        v1_math = MathTex(
            r"\lambda_1 = 2 \Rightarrow v_1 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}").scale(0.9)
        v2_math = MathTex(r"\lambda_2 = 1 \Rightarrow v_2 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}").scale(0.9)
        v3_math = MathTex(
            r"\lambda_3 = 0 \Rightarrow v_3 = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}").scale(0.9)

        top_row = VGroup(v1_math, v2_math).arrange(RIGHT, buff=2.0)

        vec_group = VGroup(top_row, v3_math) \
            .arrange(DOWN, buff=1.0) \
            .next_to(step1_cont, DOWN, buff=1.0) \
            .set_x(0)

        self.play(Write(step1_cont))
        self.wait(1.4)

        self.play(FadeIn(v1_math, shift=RIGHT))
        self.wait(3.5)

        self.play(FadeIn(v2_math, shift=LEFT))
        self.wait(1)

        self.play(FadeIn(v3_math, shift=UP))
        self.wait(1)

        self.wait(2.0)

class Scene10(Scene):
    def construct(self) -> None:
        title = Text("Bước 2: Thiết lập ma trận Σ và V", font=DEFAULT_FONT, color=BLUE) \
            .to_edge(UP, buff=0.3)

        sigma_title = Text("1. Ma trận Σ", font=DEFAULT_FONT, color=GREEN).scale(0.8)
        sigma_calc = MathTex(r"\sigma_i = \sqrt{\lambda_i}").scale(0.8)
        sigma_vals = MathTex(r"\Rightarrow \sigma_1 = \sqrt{2}, \sigma_2 = 1, \sigma_3 = 0").scale(0.8)

        note_cut = VGroup(
            Text("A cỡ 2x3 nên ", font=DEFAULT_FONT, font_size=22, color=RED),
            MathTex(r"\Sigma", color=RED).scale(0.7),
            Text(" cỡ 2x3 (cắt bỏ ", font=DEFAULT_FONT, font_size=22, color=RED),
            MathTex(r"\sigma_3", color=RED).scale(0.7),
            Text(")", font=DEFAULT_FONT, font_size=22, color=RED)
        ).arrange(RIGHT, buff=0.1)

        sigma_matrix_3x3 = MathTex(
            r"\Sigma = \begin{pmatrix} \sqrt{2} & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}"
        ).scale(0.9)

        sigma_matrix_2x3 = MathTex(
            r"\Sigma = \begin{pmatrix} \sqrt{2} & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}"
        ).scale(0.9)

        left_col = VGroup(sigma_title, sigma_calc, sigma_vals, note_cut, sigma_matrix_3x3) \
            .arrange(DOWN, buff=0.4)

        v_title = Text("2. Ma trận V", font=DEFAULT_FONT, color=GREEN).scale(0.8)
        v_calc = MathTex(r"V = \begin{pmatrix} v_1 & v_2 & v_3 \end{pmatrix}").scale(0.8)

        v_matrix = MathTex(
            r"V = \begin{pmatrix} \frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & 0 & -\frac{1}{\sqrt{2}} \\ 0 & 1 & 0 \end{pmatrix}"
        ).scale(0.8)

        right_col = VGroup(v_title, v_calc, v_matrix) \
            .arrange(DOWN, buff=0.6)

        cols = VGroup(left_col, right_col) \
            .arrange(RIGHT, buff=2.0) \
            .next_to(title, DOWN, buff=0.4)

        right_col.align_to(left_col, UP)

        divider = Line(cols.get_top() + UP * 0.2, cols.get_bottom() + DOWN * 0.2, color=GRAY)

        sigma_matrix_2x3.move_to(sigma_matrix_3x3, aligned_edge=UP)

        self.play(Write(title))
        self.wait(1.5)

        self.play(Write(sigma_title))
        self.wait(1.0)
        self.play(FadeIn(sigma_calc, shift=DOWN))
        self.play(FadeIn(sigma_vals, shift=DOWN))
        self.wait(1.5)

        self.play(Write(sigma_matrix_3x3))
        self.wait(1.5)

        self.play(FadeIn(note_cut, shift=DOWN))
        self.wait(1.5)

        self.play(ReplacementTransform(sigma_matrix_3x3, sigma_matrix_2x3))
        self.wait(2.5)

        self.play(Create(divider))
        self.wait(1.0)

        self.play(Write(v_title))
        self.wait(1.0)
        self.play(FadeIn(v_calc, shift=DOWN))
        self.wait(1.5)
        self.play(Write(v_matrix))
        self.wait(3.0)


class Scene11(Scene):
    def construct(self) -> None:

        title = Text("Bước 3: Thiết lập ma trận U", font=DEFAULT_FONT, color=BLUE) \
            .to_edge(UP, buff=0.3)

        formula = MathTex(r"u_i = \frac{1}{\sigma_i} A v_i \quad (1 \le i \le r)").scale(0.9) \
            .next_to(title, DOWN, buff=0.5)

        u1_calc = MathTex(
            r"u_1 = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}"
        ).scale(0.7)

        u2_calc = MathTex(
            r"u_2 = \frac{1}{1} \begin{pmatrix} 1 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}"
        ).scale(0.7)

        left_group = VGroup(u1_calc, u2_calc).arrange(DOWN, buff=0.5)
        u2_calc.align_to(u1_calc, LEFT)

        brace = Brace(left_group, direction=RIGHT)

        u_matrix = MathTex(
            r"U = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}"
        ).scale(0.9)

        content = VGroup(left_group, brace, u_matrix) \
            .arrange(RIGHT, buff=0.5) \
            .next_to(formula, DOWN, buff=0.8)

        box = SurroundingRectangle(formula, color = RED, buff = 0.2)
        box2 = SurroundingRectangle(u_matrix, color = GREEN, buff = 0.2)
        self.play(Write(title))
        self.wait(1.0)

        self.play(FadeIn(formula, shift=UP))
        self.wait(1.0)
        self.play(Create(box))
        self.play(FadeIn(u1_calc, shift=RIGHT))
        self.wait(0.5)

        self.play(FadeIn(u2_calc, shift=RIGHT))
        self.wait(0.5)

        self.play(GrowFromCenter(brace))
        self.play(Write(u_matrix))
        self.play(Create(box2))
        self.wait(3.0)


class Scene12(Scene):
    def construct(self) -> None:
        svd_result = MathTex(
            r"\Rightarrow A = U \Sigma V^T = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} "
            r"\begin{pmatrix} \sqrt{2} & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} "
            r"\begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ 0 & 0 & 1 \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} & 0 \end{pmatrix}"
        ).scale(0.8)

        problem_text = Text(
            "Nhưng vấn đề là ta thấy ma trận này có vẻ phức tạp hơn,\n"
            "vậy làm thế nào để ta giảm chiều dữ liệu?",
            font=DEFAULT_FONT, color=BLUE
        ).scale(0.65)

        solution_text = Text("Giải pháp:", font=DEFAULT_FONT, color=GREEN).scale(0.8)

        approx_formula = MathTex(
            r"A \approx A_k = U_k \Sigma_k V_k^T = \sum_{i=1}^{k} \sigma_i u_i v_i^T \quad (k < r)"
        ).scale(0.8)

        solution_group = VGroup(solution_text, approx_formula) \
            .arrange(RIGHT, buff=0.4) \
            .scale(0.9)

        VGroup(svd_result, problem_text, solution_group) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.5) \
            .move_to(ORIGIN)

        box = SurroundingRectangle(approx_formula, color = RED, buff = 0.2)
        self.play(FadeIn(svd_result, shift=UP))
        self.wait(3.0)

        self.play(Write(problem_text))
        self.wait(3.5)

        self.play(Write(solution_text))
        self.play(FadeIn(approx_formula, shift=RIGHT))
        self.wait(4.5)


class Scene13(Scene):
    def construct(self) -> None:

        title = Text("Giảm chiều dữ liệu với SVD", font=DEFAULT_FONT, color = YELLOW).scale(0.7)
        title.to_edge(UP, buff=0.4)

        u_start, u1, u2, u3, u_end = MathTex("U = ("), MathTex("u_1"), MathTex("u_2"), MathTex("u_3"), MathTex(")")
        U_full = VGroup(u_start, u1, u2, u3, u_end).arrange(RIGHT, buff=0.1).scale(0.7)

        Uk = MathTex(r"U_k = (u_1\ u_2)").scale(0.7)

        row_u = VGroup(U_full, Uk).arrange(RIGHT, buff=4.0)

        Sigma_full = Matrix(
            [[r"\sigma_1", "0", "0"], ["0", r"\sigma_2", "0"], ["0", "0", r"\sigma_3"]],
            left_bracket="(", right_bracket=")"
        ).scale(0.7)

        Sigma_full_labeled = VGroup(MathTex(r"\Sigma =").scale(0.7), Sigma_full).arrange(RIGHT, buff=0.1)

        Sigmak = Matrix(
            [[r"\sigma_1", "0"], ["0", r"\sigma_2"]],
            left_bracket="(", right_bracket=")"
        ).scale(0.7)
        Sigmak_labeled = VGroup(MathTex(r"\Sigma_k =").scale(0.7), Sigmak).arrange(RIGHT, buff=0.1)

        row_sigma = VGroup(Sigma_full_labeled, Sigmak_labeled).arrange(RIGHT, buff=3.5)

        Vt_full = Matrix(
            [[r"v_1^T"], [r"v_2^T"], [r"v_3^T"]],
            left_bracket="(", right_bracket=")"
        ).scale(0.7)
        Vt_full_labeled = VGroup(MathTex(r"V^T =").scale(0.7), Vt_full).arrange(RIGHT, buff=0.1)

        Vk = Matrix(
            [[r"v_1^T"], [r"v_2^T"]],
            left_bracket="(", right_bracket=")"
        ).scale(0.7)
        Vk_labeled = VGroup(MathTex(r"V_k^T =").scale(0.7), Vk).arrange(RIGHT, buff=0.1)

        row_vt = VGroup(Vt_full_labeled, Vk_labeled).arrange(RIGHT, buff=4.1)

        all_rows = VGroup(row_u, row_sigma, row_vt).arrange(DOWN, buff=0.6).shift(DOWN * 0.2)

        left_label = Text("Full (r = 3)", font=DEFAULT_FONT, color = BLUE).scale(0.5).next_to(U_full, UP, buff=0.3)
        right_label = Text("Xấp xỉ (k = 2)", font=DEFAULT_FONT, color = BLUE).scale(0.5).next_to(Uk, UP, buff=0.3)

        arrow = MathTex(r"\Longrightarrow").scale(1.1).move_to(ORIGIN).shift(RIGHT * 0.2)

        final_formula = MathTex(
            r"A \approx \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T"
        ).scale(0.8).to_edge(DOWN, buff=0.6)

        box = SurroundingRectangle(final_formula, color = RED, buff = 0.2)

        self.play(Write(title))
        self.play(FadeIn(U_full), FadeIn(Sigma_full_labeled), FadeIn(Vt_full_labeled), FadeIn(left_label))
        self.wait(1)

        s1, s2, s3 = Sigma_full.get_entries()[0], Sigma_full.get_entries()[4], Sigma_full.get_entries()[8]
        v1_t, v2_t, v3_t = Vt_full.get_entries()[0], Vt_full.get_entries()[1], Vt_full.get_entries()[2]

        self.play(
            u1.animate.set_color(GREEN), u2.animate.set_color(GREEN),
            s1.animate.set_color(GREEN), s2.animate.set_color(GREEN),
            v1_t.animate.set_color(GREEN), v2_t.animate.set_color(GREEN),
        )
        self.play(
            u3.animate.set_color(RED),
            s3.animate.set_color(RED),
            v3_t.animate.set_color(RED),
        )
        self.wait(1.5)

        self.play(Write(arrow))
        self.play(
            FadeIn(Uk, shift=LEFT),
            FadeIn(Sigmak_labeled, shift=LEFT),
            FadeIn(Vk_labeled, shift=LEFT),
            FadeIn(right_label)
        )
        self.wait(1.5)

        self.play(Write(final_formula))
        self.play(Create(box))
        self.wait(3)


class Scene14(ThreeDScene):
    def construct(self) -> None:
        DEFAULT_FONT = "Cambria"

        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # 2. TẠO ĐÁM MÂY ĐIỂM
        np.random.seed(42)
        points_pos = []
        for _ in range(150):  # Giảm số điểm để render nhanh hơn khi test
            x = np.random.normal(0, 2)
            y = np.random.normal(0, 0.6)
            z = np.random.normal(0, 0.2)
            pos = x * np.array([1, 1, 0.5]) + y * np.array([-1, 1, 0]) + z * np.array([0, 0, 1])
            points_pos.append(pos)

        dots = VGroup(*[Dot3D(point=p, radius=0.05, color=BLUE_B) for p in points_pos])

        # 3. VECTOR u1
        u1_dir = np.array([1, 1, 0.5])
        u1_dir = u1_dir / np.linalg.norm(u1_dir)
        u1_vector = Arrow3D(start=ORIGIN, end=u1_dir * 3.5, color=YELLOW)

        u1_label = MathTex("u_1", color=YELLOW)

        # 4. TEXT GIAO DIỆN (Cố định)
        title = Text("SVD: Cô đọng thông tin", font=DEFAULT_FONT, color=YELLOW).scale(0.6)
        desc1 = Text("Dữ liệu gốc (3D)", font=DEFAULT_FONT, font_size=24)
        desc2 = Text("Tìm hướng u1 quan trọng nhất", font=DEFAULT_FONT, font_size=24, color=YELLOW)
        desc3 = Text("Nén về 1D (Chiếu lên u1)", font=DEFAULT_FONT, font_size=24, color=GREEN)

        ui_group = VGroup(title, desc1, desc2, desc3).arrange(DOWN, aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(ui_group)
        ui_group.to_corner(UL).shift(DOWN * 0.3)

        desc2.set_opacity(0)
        desc3.set_opacity(0)

        # ===== ANIMATION =====
        self.add(axes)
        self.play(FadeIn(dots, lag_ratio=0.01), Write(title), Write(desc1))
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(2)

        # Xuất hiện u1
        self.play(desc1.animate.set_opacity(0.3), FadeIn(desc2))
        self.play(GrowArrow(u1_vector))

        # Đặt label u1 ở đầu mũi tên (phải update liên tục vì camera xoay)
        self.add_fixed_in_frame_mobjects(u1_label)
        u1_label.to_corner(UR, buff=1)
        self.wait(2)

        # Chiếu điểm
        self.play(desc2.animate.set_opacity(0.3), FadeIn(desc3))

        # Hiệu ứng chuyển động các điểm
        self.play(
            *[d.animate.move_to(np.dot(d.get_center(), u1_dir) * u1_dir).set_color(GREEN)
              for d in dots],
            run_time=3
        )

        self.stop_ambient_camera_rotation()
        self.wait(2)

class Scene14_1(Scene):
    """Giải thích bản chất SVD và liên hệ với nén dữ liệu"""
    def construct(self):
        title = Text("SVD thực sự đang làm gì?", font=DEFAULT_FONT, color=YELLOW)
        title.scale(0.8).to_edge(UP)
        self.play(Write(title))

        text1 = Text("Ma trận A là một phép biến đổi tuyến tính", font=DEFAULT_FONT)
        text1.scale(0.6).next_to(title, DOWN, buff=0.6)

        formula1 = MathTex("x \\rightarrow Ax").scale(1.2)
        formula1.next_to(text1, DOWN, buff=0.4)

        self.play(Write(text1))
        self.play(Write(formula1))
        self.wait(1.5)

        text2 = Text("SVD tách A thành 3 phép đơn giản", font=DEFAULT_FONT)
        text2.scale(0.6).next_to(formula1, DOWN, buff=0.6)

        formula2 = MathTex("A = U \\Sigma V^T").scale(1.2)
        formula2.next_to(text2, DOWN, buff=0.4)

        self.play(Write(text2))
        self.play(Write(formula2))
        self.wait(1.5)

        self.play(
            FadeOut(text1), FadeOut(formula1),
            FadeOut(text2), FadeOut(formula2)
        )

        text3 = Text("Không phải mọi thành phần đều quan trọng như nhau", font=DEFAULT_FONT)
        text3.scale(0.6).next_to(title, DOWN, buff=0.6)

        self.play(Write(text3))

        sigma = MathTex("\\sigma_1 > \\sigma_2 > \\sigma_3 > \\dots").scale(1.2)
        sigma.next_to(text3, DOWN, buff=0.5)

        self.play(Write(sigma))
        self.wait(1.5)

        box1 = SurroundingRectangle(sigma[0:3], color=GREEN, buff=0.2)
        self.play(Create(box1))
        self.wait(1)

        approx = MathTex(
            "A_k = \\sum_{i=1}^{k} \\sigma_i u_i v_i^T"
        ).scale(1.2)

        approx.next_to(sigma, DOWN, buff=0.8)

        self.play(Write(approx))
        self.wait(1.5)

        self.play(
            FadeOut(text3),
            FadeOut(sigma),
            FadeOut(box1),
            FadeOut(approx)
        )

        insight = Text(
            "Giữ hướng quan trọng → Bỏ hướng ít quan trọng",
            font=DEFAULT_FONT,
            color=LIGHTBLUE
        ).scale(0.7)

        insight.next_to(title, DOWN, buff=1)

        self.play(Write(insight))
        self.wait(2)

        image_text = Text(
            "→ Đó chính là lý do ta có thể nén ảnh và giảm chiều dữ liệu",
            font=DEFAULT_FONT
        ).scale(0.6)

        image_text.next_to(insight, DOWN, buff=0.8)

        self.play(Write(image_text))
        self.wait(2)


class Scene15(Scene):
    def construct(self) -> None:
        title = Text("SVD: Nén và Tái tạo ảnh Albert Einstein", font=DEFAULT_FONT, color=YELLOW).scale(0.8)
        title.to_edge(UP, buff=0.3)

        k10 = ImageMobject("k10.png").set_resampling_algorithm(RESAMPLING_ALGORITHMS["bilinear"])
        k25 = ImageMobject("k25.png").set_resampling_algorithm(RESAMPLING_ALGORITHMS["bilinear"])
        k50 = ImageMobject("k50.png").set_resampling_algorithm(RESAMPLING_ALGORITHMS["bilinear"])
        k100 = ImageMobject("k100.jpg").set_resampling_algorithm(RESAMPLING_ALGORITHMS["bilinear"])

        for img in [k10, k25, k50, k100]:
            img.height = 4
            img.center()

        slider_line = Line(LEFT * 3, RIGHT * 3, color=GRAY).to_edge(DOWN, buff=1.2)
        slider_dot = Dot(color=YELLOW).move_to(slider_line.get_start())

        k_label = Text("Giá trị k = ", font=DEFAULT_FONT, font_size=28)
        k_value = Integer(10, font_size=28).next_to(k_label, RIGHT)
        k_group = VGroup(k_label, k_value).next_to(slider_line, UP, buff=0.5)

        def update_k(obj):
            prop = (slider_dot.get_x() - slider_line.get_start()[0]) / slider_line.get_width()
            val = int(10 + prop * 90)
            k_value.set_value(val)
            k_group.next_to(slider_dot, UP, buff=0.3)

        k_group.add_updater(update_k)

        self.add(title, slider_line, slider_dot, k_group)
        self.play(FadeIn(k10))
        self.wait(1)

        targets = [(25, k25), (50, k50), (100, k100)]

        current_img = k10
        for val, next_img in targets:
            self.play(
                slider_dot.animate.move_to(slider_line.point_from_proportion((val - 10) / 90)),
                run_time=1.5
            )
            self.play(FadeOut(current_img), FadeIn(next_img), run_time=0.4)
            current_img = next_img
            self.wait(0.5)

        self.wait(2)

class Scene16(ThreeDScene):
    """Trực quan hóa SVD: rotate → scale → rotate"""

    def construct(self):
        title = Text("Trực quan hình học của SVD", font=DEFAULT_FONT, color=YELLOW)
        title.scale(0.8).to_edge(UP)
        self.play(Write(title))

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
        ).shift(DOWN * 0.5)

        grid = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_opacity": 0.3
            }
        ).match_width(axes).move_to(axes)

        self.play(Create(grid), Create(axes))
        circle = Circle(radius=1.5, color=BLUE)
        circle.move_to(axes.c2p(0, 0))

        label_circle = Text("Unit Circle", font=DEFAULT_FONT).scale(0.5)
        label_circle.next_to(circle, DOWN)

        dot = Dot(color=YELLOW).scale(0.8)
        dot.move_to(circle.point_at_angle(0))

        self.play(Create(circle), FadeIn(label_circle), FadeIn(dot))
        self.wait(1)

        step1_text = MathTex("V^T: \\text{Rotate}", color=GREEN).scale(0.7)
        step1_text.to_edge(RIGHT).shift(UP * 1.5)

        self.play(Write(step1_text))

        rotated_circle = circle.copy().set_color(GREEN)

        rotated_dot = dot.copy()

        self.play(
            Rotate(rotated_circle, angle=PI/6, about_point=axes.c2p(0, 0)),
            Rotate(rotated_dot, angle=PI/6, about_point=axes.c2p(0, 0)),
            run_time=2
        )
        self.wait(1)
        step2_text = MathTex("\\Sigma: \\text{Scale}", color=ORANGE).scale(0.7)
        step2_text.next_to(step1_text, DOWN, aligned_edge=LEFT)

        self.play(Write(step2_text))

        ellipse = rotated_circle.copy().set_color(ORANGE)
        ellipse_dot = rotated_dot.copy()

        self.play(
            ellipse.animate.stretch(2, 0).stretch(0.5, 1),
            ellipse_dot.animate.stretch(2, 0).stretch(0.5, 1),
            run_time=2
        )
        self.wait(1)

        step3_text = MathTex("U: \\text{Rotate}", color=PURPLE).scale(0.7)
        step3_text.next_to(step2_text, DOWN, aligned_edge=LEFT)

        self.play(Write(step3_text))

        final_shape = ellipse.copy().set_color(PURPLE)
        final_dot = ellipse_dot.copy()

        self.play(
            Rotate(final_shape, angle=-PI/4, about_point=axes.c2p(0, 0)),
            Rotate(final_dot, angle=-PI/4, about_point=axes.c2p(0, 0)),
            run_time=2
        )
        self.wait(1)

        formula = MathTex("A = U \\Sigma V^T").scale(1.2)
        formula.to_edge(DOWN)

        self.play(Write(formula))
        self.wait(2)
class Scene1_1(Scene):
    """Bổ sung phân mở đầu: Nhắc lại chéo hóa và giới thiệu bài toán"""

    def construct(self):
        title_diag = Text("Chéo hóa ma trận vuông", font=DEFAULT_FONT, color = YELLOW).scale(0.8).to_edge(UP)
        self.play(Write(title_diag))

        matrix_A_square = MathTex("A", "=", "\\begin{bmatrix} 4 & 1 \\\\ 2 & 3 \\end{bmatrix}")
        matrix_A_square.next_to(title_diag, DOWN, buff=0.5)
        self.play(FadeIn(matrix_A_square))
        self.wait(1)

        eigen_info = MathTex(
            "\\lambda_1 = 5, v_1 = \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}",
            "\\quad",
            "\\lambda_2 = 2, v_2 = \\begin{bmatrix} -1 \\\\ 2 \\end{bmatrix}"
        ).scale(0.9).next_to(matrix_A_square, DOWN, buff=0.4)
        self.play(Write(eigen_info))
        self.wait(1)

        diag_formula = MathTex("A", "=", "P", "D", "P^{-1}")
        diag_expanded = MathTex(
            "\\begin{bmatrix} 4 & 1 \\\\ 2 & 3 \\end{bmatrix}", "=",
            "\\begin{bmatrix} 1 & -1 \\\\ 1 & 2 \\end{bmatrix}",
            "\\begin{bmatrix} 5 & 0 \\\\ 0 & 2 \\end{bmatrix}",
            "\\begin{bmatrix} 1 & -1 \\\\ 1 & 2 \\end{bmatrix}^{-1}"
        ).scale(0.8)

        group_diag = VGroup(diag_formula, diag_expanded).arrange(DOWN, buff=0.3).next_to(eigen_info, DOWN, buff=0.4)
        box1 = SurroundingRectangle(diag_formula, color=RED, buff=0.2)
        self.play(Write(diag_formula))
        self.play(Create(box1))
        self.play(TransformMatchingTex(diag_formula.copy(), diag_expanded))
        self.wait(2)

        self.play(
            FadeOut(title_diag),
            FadeOut(matrix_A_square),
            FadeOut(eigen_info),
            FadeOut(group_diag),
            FadeOut(box1)
        )

        question = Text("Nếu ma trận không vuông thì sao?", font=DEFAULT_FONT, color = LIGHTBLUE).scale(0.9)
        self.play(Write(question))
        self.wait(1.5)
        self.play(question.animate.to_edge(UP).scale(0.8))

        matrix_A_rect = MathTex("A", "=", "\\begin{bmatrix} 3 & 2 & 2 \\\\ 2 & 3 & -2 \\end{bmatrix}")
        matrix_A_rect.next_to(question, DOWN, buff=0.8)
        self.play(FadeIn(matrix_A_rect))
        self.wait(1)

        svd_title = Text("Phân rã SVD", font=DEFAULT_FONT).scale(0.8).next_to(matrix_A_rect, DOWN, buff=0.6)
        svd_formula = MathTex("A", "=", "U", "\\Sigma", "V^T").scale(1.5).next_to(svd_title, DOWN, buff=0.4)
        box2 = SurroundingRectangle(svd_formula, color = RED, buff = 0.2)
        self.play(Write(svd_title))
        self.play(Write(svd_formula))
        self.play(Create(box2))
        self.wait(2)

class Scene16_1(Scene):
    def construct(self):
        title = Text("Ma trận A thực sự là gì?", font=DEFAULT_FONT, color=YELLOW)
        title.scale(0.8).to_edge(UP)
        self.play(Write(title))

        subtitle = Text(
            "Ma trận A có thể coi là dữ liệu hoặc cũng có thể coi là một phép biến đổi",
            font=DEFAULT_FONT
        ).scale(0.5)

        subtitle.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle))
        left_title = Text("A là một phép biến đổi", font=DEFAULT_FONT, color=BLUE).scale(0.6)

        mapping = MathTex("x", "\\rightarrow", "Ax").scale(0.9)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=3.5,
            y_length=3.5,
        )

        vec_x = Arrow(axes.c2p(0, 0), axes.c2p(1, 1), color=BLUE, buff=0)
        label_x = MathTex("x").scale(0.6).next_to(vec_x.get_end(), RIGHT)

        vec_Ax = Arrow(axes.c2p(0, 0), axes.c2p(2.5, 1), color=ORANGE, buff=0)
        label_Ax = MathTex("Ax").scale(0.6).next_to(vec_Ax.get_end(), UP)

        left_group = VGroup(left_title, mapping, axes).arrange(DOWN, buff=0.3)
        left_group.next_to(subtitle, DOWN, buff=0.6).to_edge(LEFT, buff=0.8)
        right_title = Text("A là dữ liệu (ảnh)", font=DEFAULT_FONT, color=GREEN).scale(0.6)

        image = ImageMobject("k100.jpg").scale(0.6)

        fake_matrix = MathTex(
            "A", "=",
            "\\begin{bmatrix}"
            "12 & 45 & 78 \\\\"
            "34 & 90 & 123 \\\\"
            "56 & 67 & 89"
            "\\end{bmatrix}"
        ).scale(0.7)

        right_group = Group(right_title, image)
        right_group.arrange(DOWN, buff=0.3)
        right_group.next_to(subtitle, DOWN, buff=0.6).to_edge(RIGHT, buff=0.8)

        self.play(Write(left_title), Write(right_title))
        self.play(Write(mapping), FadeIn(image))
        self.play(Create(axes))

        self.play(GrowArrow(vec_x), Write(label_x))
        self.wait(0.5)

        self.play(
            Transform(vec_x, vec_Ax),
            Transform(label_x, label_Ax),
            run_time=2
        )

        self.play(Transform(image, fake_matrix), run_time=2)


        insight = Text(
            "Cùng một ma trận A, ta có hai cách nhìn khác nhau",
            font=DEFAULT_FONT,
            color=LIGHTBLUE
        ).scale(0.5)

        insight.to_edge(DOWN)

        self.play(Write(insight))
        self.wait(2)

class BS1(Scene):
    def construct(self):
        main_title = Text("Bản chất cốt lõi của SVD: Phân tách thông tin", color=YELLOW_D, font=DEFAULT_FONT).scale(0.8)
        self.play(Write(main_title))
        self.wait(1)
        self.play(main_title.animate.to_corner(UL).scale(0.7))

        geo_title = Text("Góc nhìn Hình học", color=GREEN, font=DEFAULT_FONT).scale(0.6)
        geo_subtitle = Text("(Ma trận A là 'Hành động')", color=GRAY, font=DEFAULT_FONT).scale(0.5)
        VGroup(geo_title, geo_subtitle).arrange(DOWN, buff=0.1).to_edge(LEFT, buff=1).shift(UP * 2)

        axes = Axes(x_range=[-2.5, 2.5, 1], y_range=[-2.5, 2.5, 1], x_length=3, y_length=3,
                    axis_config={"include_tip": False})
        circle = Circle(radius=1.2, color=GREEN).move_to(axes.c2p(0, 0))
        geo_visual = VGroup(axes, circle).next_to(geo_subtitle, DOWN, buff=0.5)

        transformed_circle = circle.copy().stretch(2, dim=0).stretch(0.5, dim=1).rotate(PI / 6).set_color(GREEN_E)

        data_title = Text("Góc nhìn Dữ liệu", color=ORANGE, font=DEFAULT_FONT).scale(0.6)
        data_subtitle = Text("(Ma trận A là 'Vật thể tĩnh')", color=GRAY, font=DEFAULT_FONT).scale(0.5)
        VGroup(data_title, data_subtitle).arrange(DOWN, buff=0.1).to_edge(RIGHT, buff=1).shift(UP * 2)

        matrix_X = np.array([
            [1.0, 0.2, 0.2, 1.0],
            [0.2, 1.0, 1.0, 0.2],
            [0.2, 1.0, 1.0, 0.2],
            [1.0, 0.2, 0.2, 1.0]
        ])

        photo_grid = VGroup(*[
            Rectangle(width=0.6, height=0.6, fill_opacity=matrix_X[i, j], fill_color=WHITE, stroke_color=GRAY,
                      stroke_width=0.5)
            for i in range(4) for j in range(4)
        ]).arrange_in_grid(rows=4, cols=4, buff=0.02).next_to(data_subtitle, DOWN, buff=0.5)

        self.play(Write(geo_title), Write(geo_subtitle), Write(data_title), Write(data_subtitle))
        self.play(FadeIn(geo_visual), FadeIn(photo_grid))
        self.wait(1)

        self.play(ReplacementTransform(circle, transformed_circle, run_time=2, rate_func=smooth))
        self.wait(1)

        text_geo_is_A = MathTex("f(x) = Ax").next_to(geo_visual, DOWN, buff=0.2).scale(0.8).set_color(GREEN)
        text_data_is_A = Text("A = [Ma trận điểm ảnh]", color=ORANGE, font=DEFAULT_FONT).next_to(photo_grid, DOWN,
                                                                                                 buff=0.2).scale(0.5)

        self.play(Write(text_geo_is_A), Write(text_data_is_A))
        self.wait(1)

        matrix_content = DecimalMatrix(
            [[1.2, 0.8], [0.3, 1.5]],
            element_to_mobject_config={"num_decimal_places": 1, "color": GRAY_C},
            bracket_h_buff=0.1
        )
        label_A = Text("Ma trận A", color=BLUE, font=DEFAULT_FONT).scale(0.6).next_to(matrix_content, UP, buff=0.2)
        group_A_matrix = VGroup(label_A, matrix_content).move_to(ORIGIN).shift(UP * 1)

        self.play(
            FadeOut(geo_title), FadeOut(geo_subtitle), FadeOut(data_title), FadeOut(data_subtitle),
            FadeOut(geo_visual), FadeOut(transformed_circle), FadeOut(text_geo_is_A),
            FadeOut(photo_grid), FadeOut(text_data_is_A),
            run_time=1.5
        )
        self.play(FadeIn(group_A_matrix))
        self.wait(1)

        self.play(group_A_matrix.animate.shift(LEFT * 3.5).scale(0.8))

        equals_sign = MathTex("=").next_to(group_A_matrix, RIGHT, buff=0.3).scale(1.5)
        self.play(Write(equals_sign))

        term1 = MathTex(r"\sigma_1 \mathbf{u}_1 \mathbf{v}_1^T", color=WHITE).scale(1.1)
        term2 = MathTex(r"\sigma_2 \mathbf{u}_2 \mathbf{v}_2^T", color=GRAY_A).scale(0.8)
        term3 = MathTex(r"...", color=GRAY_C).scale(0.7)
        plus1 = MathTex("+").scale(1)
        plus2 = MathTex("+").scale(1)

        decomposition_sum = VGroup(term1, plus1, term2, plus2, term3).arrange(RIGHT, buff=0.2).next_to(equals_sign,
                                                                                                       RIGHT, buff=0.3)

        self.play(Write(decomposition_sum[0]))
        self.play(Write(decomposition_sum[1]), Write(decomposition_sum[2]))
        self.play(Write(decomposition_sum[3]), Write(decomposition_sum[4]))
        self.wait(1)

        label_sigma_text = Text(": Lượng thông tin", color=YELLOW_D, font=DEFAULT_FONT).scale(0.4)
        label_sigma = VGroup(MathTex(r"\sigma_i", color=YELLOW_D).scale(0.8), label_sigma_text).arrange(RIGHT,
                                                                                                        buff=0.1).next_to(
            term1, UP, buff=0.5).shift(LEFT * 0.5)
        line_sigma = Arrow(label_sigma.get_bottom(), term1[0][0].get_top(), color=YELLOW_D, buff=0.1, tip_length=0.1)

        label_rank1_text = Text(": Đặc trưng cơ bản", color=BLUE_B, font=DEFAULT_FONT).scale(0.4)
        label_rank1 = VGroup(MathTex(r"\mathbf{u}_i \mathbf{v}_i^T", color=BLUE_B).scale(0.8),
                             label_rank1_text).arrange(RIGHT, buff=0.1).next_to(term1, DOWN, buff=0.5)
        line_rank1 = Arrow(label_rank1.get_top(), term1[0][1:7].get_bottom(), color=BLUE_B, buff=0.1, tip_length=0.1)

        self.play(FadeIn(label_sigma), GrowArrow(line_sigma))
        self.play(FadeIn(label_rank1), GrowArrow(line_rank1))
        self.wait(1)

        self.play(FadeOut(label_sigma), FadeOut(line_sigma), FadeOut(label_rank1), FadeOut(line_rank1),
                  )

        def_rect = Rectangle(width=12, height=2.5, color=BLUE_E).to_edge(DOWN, buff=0.2)
        def_title = Text("Bản chất Đại số của SVD:", color=BLUE_B, font=DEFAULT_FONT).scale(0.6).next_to(
            def_rect.get_top(), DOWN, buff=0.2)

        bullet1 = Text("- Phân tách thông tin thành tổng các mảnh ghép đơn giản nhất (Hạng 1).",
                       font=DEFAULT_FONT).scale(0.4)
        bullet2 = Text("- Sắp xếp các mảnh ghép theo mức độ quan trọng giảm dần.", font=DEFAULT_FONT).scale(0.4)
        bullet3 = Text("- Giá trị kỳ dị là thước đo lượng thông tin của mảnh ghép.", font=DEFAULT_FONT).scale(0.4)

        def_text = VGroup(bullet1, bullet2, bullet3).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(def_title, DOWN,
                                                                                                        buff=0.2)

        self.play(Create(def_rect), Write(def_title))
        self.play(Write(def_text))
        self.wait(3)
