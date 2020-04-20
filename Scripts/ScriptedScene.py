LoadScript("classes/BiconvexLens.py")

scene = Scene()
biconvex_lens_node = BiconvexLens()
scene.AddNode(biconvex_lens_node)
LoadScene(scene)