class BiconvexLens(PNode):
    h = Param("Semi diameter", Size, 2)
    r = Param("Radius", Size, 5)
    length = Param("Length", Size, 1)

    def Init(self):
        AsphericalSurface = GetClass(Shape, 'Aspherical Surface')
        Cylinder = GetClass(Shape, 'Cylinder')

        firstSurface = AsphericalSurface(h=self.h, h0=0, r=self.r)
        firstSurface_node = MeshNode(firstSurface, name="FirstSurface")
        firstSurface_node.Translate(0, 0, 0)

        cylinderSurface = Cylinder(radius=self.r / 2, length=self.length)        
        cylinderSurface_node = MeshNode(cylinderSurface, name="CylinderSurface")
        cylinderSurface_node.Translate(0, 0, 0)

        secondSurface = AsphericalSurface(h=self.h, h0=0, r=-self.r)
        secondSurface_node = MeshNode(secondSurface, name="SecondSurface")
        secondSurface_node.Translate(0, 0, 0)

        self.SetChildren( [ firstSurface_node, cylinderSurface_node, secondSurface_node ] )

    def Eval(self):
        pass