import sysconfig
from pathlib import Path


def main() -> None:
    site_packages = Path(sysconfig.get_paths()["purelib"])
    isaacsim_dir = site_packages / "isaacsim"

    extension_roots = [
        isaacsim_dir / "extscache",
        isaacsim_dir / "exts",
        isaacsim_dir / "extsDeprecated",
        isaacsim_dir / "kit" / "extscore",
    ]

    paths = set()

    for root in extension_roots:
        if not root.is_dir():
            continue

        for extension in root.iterdir():
            if extension.is_dir() and any(
                    (extension / package).is_dir()
                    for package in ("omni", "isaacsim")
            ):
                paths.add(extension.relative_to(site_packages).as_posix())

    kit_python = isaacsim_dir / "kit" / "kernel" / "py"
    if (kit_python / "omni").is_dir():
        paths.add(kit_python.relative_to(site_packages).as_posix())

    if not paths:
        raise RuntimeError(f"No extension roots found under {isaacsim_dir}")

    pth_file = site_packages / "isaacsim_extension_paths.pth"
    pth_file.write_text("\n".join(sorted(paths)) + "\n", encoding="utf-8")

    print(f"Configured {len(paths)} extension paths in {pth_file}")
    print("Restart your IDE to refresh indexing.")


if __name__ == "__main__":
    main()
