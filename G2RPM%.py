# G2RPM%.py
# Convert G's (acceleration) to RPM and interpret percentage as RPM in VSPIN range (0-3000 RPM)
# This can be updated to include any Hamilton integrated centrifuges for quick conversion.

import math
# Function objective: convert G's to RPM and ask for user input for radius in meters.
def gs_to_rpm(gs, radius_cm):
    
    # Convert G's to RPM given the radius in meters.
    # Formula: RPM = sqrt((G * 9.80665) / (r * (2 * pi)^2)) * 60
    # Rearranged: RPM = sqrt((gs * 9.80665) / radius_m) / (2 * math.pi) * 60
    
    if radius_cm <= 0:
        raise ValueError("Radius must be positive and a Integer.")
    rpm = math.sqrt((gs * 9.80665) / radius_cm) / (2 * math.pi) * 60
    return rpm

def rpm_to_percent(rpm, max_rpm=3000):
    
    # Convert an RPM value in the VSPIN range (0-max_rpm) to a percentage (0-100).
    
    if not (0 <= rpm <= max_rpm):
        raise ValueError(f"RPM must be between 0 and {max_rpm}.")
    return (rpm / max_rpm) * 100

def main():
    print("G's to RPM Converter and VSPIN RPM to Percentage Interpreter")
    mode = input("Choose mode: (1) G's to RPM, (2) RPM to %: ").strip()
    if mode == '1':
        gs = float(input("Enter G's (acceleration): "))
        radius = float(input("Enter radius in meters: "))
        rpm = gs_to_rpm(gs, radius)
        print(f"{gs} G's at {radius} m radius = {rpm:.2f} RPM")
    elif mode == '2':
        rpm = float(input("Enter RPM (0-3000): "))
        percent = rpm_to_percent(rpm)
        print(f"{rpm} RPM = {percent:.2f}% (VSPIN range 0-3000 RPM)")
    else:
        print("Please Enter a valid choice.")

if __name__ == "__main__":
    main()