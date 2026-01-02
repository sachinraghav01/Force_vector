"""This is the solution  for task  , addition  of N number of force vectors given
by magnitude and angle, calculates the resulting force, and
   draws the force polygon diagram."""




import math
import matplotlib.pyplot as plt
n = int(input("Enter the number of forces : "))

#  store force components of x-axis and y axis
forces_x = []
forces_y = []

# Input force data
for i in range(n):
    print(f"\nForce {i + 1}:")
    magnitude = float(input("  Enter magnitude (N): "))
    angle_deg = float(input("  Enter angle (degrees): "))

    # Convert angle degree to radians
    angle_rad = math.radians(angle_deg)

    # Calculate x and y components
    fx = magnitude * math.cos(angle_rad)
    fy = magnitude * math.sin(angle_rad)

    forces_x.append(fx)
    forces_y.append(fy)

# Resultant force components
resultant_x = sum(forces_x)
resultant_y = sum(forces_y)

# Resultant magnitude and angle
resultant_magnitude = math.sqrt(resultant_x**2 + resultant_y**2)
resultant_angle = math.degrees(math.atan2(resultant_y, resultant_x))

# Output results
print("\nResultant Force:")
print(f"  Magnitude: {resultant_magnitude:.2f} N")
print(f"  Angle: {resultant_angle:.2f} degrees")

#  force polygon on graph

x_points = [0]
y_points = [0]

# Here i am creating  force polygon points
for fx, fy in zip(forces_x, forces_y):
    x_points.append(x_points[-1] + fx)
    y_points.append(y_points[-1] + fy)

plt.figure()
plt.plot(x_points, y_points, marker='o', label="Force Polygon")

# Plot resultant force
plt.arrow(0, 0, resultant_x, resultant_y,
          head_width=0.05 * resultant_magnitude,
          length_includes_head=True,
          color='red',
          label="Resultant Force")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Force Vector Addition (Force Polygon)")
plt.grid(True)
plt.axis("equal")
plt.legend()

# Save the figure
plt.savefig("force_polygon.png")
plt.show()

print("\nForce polygon diagram saved as 'force_polygon.png'")
