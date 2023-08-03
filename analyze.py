import trimesh
import sys

class STLAnalyzer:
    def __init__(self, file_path):
        """
        Initialize the STLAnalyzer with the file path of the STL file.
        """
        try:
            # Load the mesh from the STL file
            self.mesh = trimesh.load_mesh(file_path)
        except Exception as e:
            print(f"Failed to load mesh: {e}")
            sys.exit(1)

    def get_vertices(self):
        """
        Returns the vertices of the STL file's mesh.
        """
        return self.mesh.vertices

    def get_edges(self):
        """
        Returns the edges of the STL file's mesh.
        """
        return self.mesh.edges

    def get_faces(self):
        """
        Returns the faces of the STL file's mesh.
        """
        return self.mesh.faces

    def get_volume(self):
        """
        Returns the volume of the STL file's mesh.
        """
        if not self.mesh.is_watertight:
            print("Warning: Mesh is not watertight, volume calculation may be incorrect.")
        return self.mesh.volume

    def get_surface_area(self):
        """
        Returns the surface area of the STL file's mesh.
        """
        return self.mesh.area

    def get_mass_properties(self):
        """
        Returns the mass properties of the STL file's mesh.
        """
        if not self.mesh.is_watertight:
            print("Warning: Mesh is not watertight, mass properties may be incorrect.")
        return self.mesh.mass_properties

    def print_properties(self):
        """
        Prints the properties of the STL file's mesh.
        """
        print('Vertices:', len(self.get_vertices()))
        print('Edges:', len(self.get_edges()))
        print('Faces:', len(self.get_faces()))
        print('Volume:', self.get_volume())
        print('Surface area:', self.get_surface_area())
        print('Mass properties:', self.get_mass_properties())

    def visualize_mesh(self):
        """
        Visualize the STL file's mesh.
        """
        self.mesh.show()


if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python analyze_stl.py <stl_file>")
        sys.exit(1)

    # Create an STLAnalyzer for the given STL file
    stl_analyzer = STLAnalyzer(sys.argv[1])

    # Print the properties of the STL file's mesh
    stl_analyzer.print_properties()

    # Visualize the STL file's mesh
    stl_analyzer.visualize_mesh()
