import flet as ft
import time

class StatsTracker:
    def __init__(self):
        self.reset()

    def reset(self):
        self.start_time = None
        self.errors = 0

    def start(self):
        self.start_time = time.time()

    def get_wpm(self, current_idx):
        if not self.start_time: return 0
        elapsed = (time.time() - self.start_time) / 60
        return (current_idx / 5) / elapsed if elapsed > 0 else 0

    def get_accuracy(self, current_idx):
        total = current_idx + self.errors
        return (current_idx / total * 100) if total > 0 else 100

class SpeedTestApp:
    def __init__(self):
        self.text = ""
        self.current_idx = 0
        self.stats = StatsTracker()
        self.generate_new_text_callback = None 

    async def main(self, page: ft.Page):
        self.page = page
        self.page.title = "Typing Speed Test AI"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window_width = 1000
        self.page.window_height = 800
        self.page.bgcolor = "#F5F7FA"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.padding = 40
        
        # Настройка шрифтов
        self.page.fonts = {
            "Roboto Mono": "raw.githubusercontent.com"
        }

        self.loader = ft.ProgressBar(width=400, color=ft.Colors.BLUE_600, visible=False, border_radius=10)
        
        self.text_container = ft.Container(
            content=self.build_text_display(),
            padding=30,
            bgcolor=ft.Colors.WHITE,
            border_radius=20,
            shadow=ft.BoxShadow(blur_radius=20, color="#DEE2E6"),
            animate=ft.Animation(600, ft.AnimationCurve.DECELERATE)
        )

        self.input_field = ft.TextField(
            label="Текст генерируется...",
            on_change=self.on_change,
            disabled=True,
            border_radius=15,
            text_size=18,
            bgcolor=ft.Colors.WHITE,
            content_padding=20,
        )

        # статистика
        self.wpm_card = self._create_stat_card("WPM", "0", ft.Icons.SPEED, ft.Colors.ORANGE_500)
        self.acc_card = self._create_stat_card("Точность", "100%", ft.Icons.CHECK_CIRCLE, ft.Colors.GREEN_500)
        self.err_card = self._create_stat_card("Ошибки", "0", ft.Icons.ERROR_OUTLINE, ft.Colors.RED_500)

        # Кнопки
        self.gen_button = ft.ElevatedButton(
            "Сгенерировать текст (ИИ)",
            icon=ft.Icons.AUTO_AWESOME,
            style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_600, shape=ft.RoundedRectangleBorder(radius=10)),
            on_click=self.handle_generate_click
        )

        self.page.add(
            ft.Column([
                ft.Text("Typing Speed Test", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                self.loader,
                self.text_container,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                self.input_field,
                ft.Row([
                    self.gen_button,
                    ft.IconButton(ft.Icons.REFRESH_ROUNDED, on_click=self.handle_reset, tooltip="Сбросить ввод"),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self.wpm_card, self.acc_card, self.err_card], spacing=20)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        self.page.update()

    def _create_stat_card(self, label, value, icon, color):
        return ft.Container(
            content=ft.Column([
                ft.Icon(icon, color=color, size=30),
                ft.Text(value, size=24, weight="bold", color=ft.Colors.BLUE_900),
                ft.Text(label.upper(), size=12, color=ft.Colors.BLUE_GREY_400),
            ], horizontal_alignment="center", spacing=5),
            bgcolor=ft.Colors.WHITE, padding=20, border_radius=15, expand=True,
            shadow=ft.BoxShadow(blur_radius=10, color="#E9ECEF")
        )

    async def handle_generate_click(self, e):
        if self.generate_new_text_callback:
            self.gen_button.disabled = True
            self.input_field.disabled = True
            self.loader.visible = True
            self.text = ""
            self.update_ui()
            await self.generate_new_text_callback()
            self.gen_button.disabled = False
            self.page.update()

    async def set_text(self, new_text):
        self.text = new_text.strip()
        self.current_idx = 0
        self.stats.reset()
        self.input_field.disabled = False
        self.input_field.value = ""
        self.input_field.label = "Начинайте печатать..."
        self.loader.visible = False
        self.update_ui()
        await self.input_field.focus()

    async def on_change(self, e):
        val = self.input_field.value
        if not self.stats.start_time and val:
            self.stats.start()

        if len(val) > self.current_idx:
            if self.current_idx < len(self.text) and val[-1] == self.text[self.current_idx]:
                self.current_idx += 1
            else:
                self.stats.errors += 1
                self.input_field.value = val[:-1]
        else:
            self.current_idx = len(val)

        self.update_ui()
        if self.current_idx == len(self.text) and len(self.text) > 0:
            await self.finish()

    def update_ui(self):
        self.text_container.content = self.build_text_display()
        acc = self.stats.get_accuracy(self.current_idx)
        wpm = self.stats.get_wpm(self.current_idx)
        self.wpm_card.content.controls[1].value = f"{wpm:.0f}"
        self.acc_card.content.controls[1].value = f"{acc:.0f}%"
        self.err_card.content.controls[1].value = f"{self.stats.errors}"
        self.page.update()

    def build_text_display(self):
        if not self.text:
            return ft.Row([ft.ProgressRing(width=20, height=20, stroke_width=2), ft.Text(" Генерируем текст(это займет много времени)...")], alignment="center")
        return ft.Text(
            font_family="Roboto Mono",
            spans=[
                ft.TextSpan(self.text[:self.current_idx], ft.TextStyle(color=ft.Colors.GREEN_600, size=22, weight="w500")),
                ft.TextSpan(self.text[self.current_idx:self.current_idx+1], ft.TextStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_600, size=24, weight="bold")),
                ft.TextSpan(self.text[self.current_idx+1:], ft.TextStyle(color=ft.Colors.BLUE_GREY_700, size=22)),
            ]
        )

    async def finish(self):
        wpm = self.stats.get_wpm(self.current_idx)
        self.input_field.disabled = True
        dlg = ft.AlertDialog(
            title=ft.Text("Тест завершен!"),
            content=ft.Text(f"Ваша скорость: {wpm:.1f} WPM"),
            actions=[ft.TextButton("ОК", on_click=lambda _: self.close_dlg(dlg))]
        )
        self.page.overlay.append(dlg)
        dlg.open = True
        self.page.update()

    def close_dlg(self, dlg):
        dlg.open = False
        self.page.update()

    async def handle_reset(self, e):
        self.stats.reset()
        self.current_idx = 0
        self.input_field.value = ""
        self.update_ui()
        await self.input_field.focus()
