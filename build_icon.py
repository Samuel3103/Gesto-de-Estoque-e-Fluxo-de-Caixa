from pathlib import Path

from PIL import Image, ImageDraw, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "logo-cafe-biscoito.png"
PNG_OUTPUT = ROOT / "assets" / "app-icon.png"
ICO_OUTPUT = ROOT / "assets" / "app-icon.ico"


def build_icon() -> None:
    logo = Image.open(SOURCE).convert("RGB")
    logo = ImageOps.fit(logo, (512, 512), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))

    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    mask = Image.new("L", (512, 512), 0)
    ImageDraw.Draw(mask).rounded_rectangle((4, 4, 508, 508), radius=84, fill=255)
    canvas.paste(logo, (0, 0), mask)

    canvas.save(PNG_OUTPUT, format="PNG", optimize=True)
    canvas.save(
        ICO_OUTPUT,
        format="ICO",
        sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)],
    )


if __name__ == "__main__":
    build_icon()
