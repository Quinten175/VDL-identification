from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})
import omni.replicator.core as rep

writer = rep.WriterRegistry.get("BasicWriter")
writer.initialize(
    output_dir=[],
    rgb=True,
    semantic_segmentation=True,
    colorize_semantic_segmentation=True,
)