from plyfile import PlyData

# ply = PlyData.read("/mnt/A/jiangzy/datasets/garden/checkpoint/point_cloud/iteration_30000/point_cloud.ply")
ply = PlyData.read("/mnt/A/jiangzy/TIP-Editor/res_gaussion/colmap_doll/refine_res/ply/edited_ep0072.ply")

print(ply)