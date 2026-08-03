# Kimi K3 Electric Scooter Annual Operating Cost Calculator

# --- Scooter Technical Specifications (Estimates for Kimi K3) ---
BATTERY_CAPACITY_KWH = 0.36  # Kimi K3 typically has a 36V 10Ah battery = 360 Wh = 0.36 kWh
RANGE_KM_PER_CHARGE = 30   # Estimated range on a full charge (can vary)
CHARGING_EFFICIENCY = 0.85 # 85% efficiency (15% energy loss during charging)

# --- Cost Parameters (Example values, can be adjusted) ---
ELECTRICITY_PRICE_TL_PER_KWH = 2.50 # Average electricity price in TL per kWh (e.g., ~2.5 TL/kWh)
MAINTENANCE_COST_PER_KM_TL = 0.10  # Estimated maintenance cost per km (tires, brakes, minor checks)
ANNUAL_INSURANCE_TL = 300   # Estimated annual insurance/legal obligation cost
ANNUAL_MISC_PARTS_TL = 150  # Estimated annual cost for minor spare parts (e.g., lights, grips)

def calculate_annual_cost(annual_distance_km):
    """
    Calculates the estimated annual operating cost for the Kimi K3 scooter.
    """
    print(f"\n--- Yıllık İşletme Maliyeti Hesaplaması ({annual_distance_km} km) ---")

    # 1. Calculate Energy Consumption and Cost
    # Energy needed from the grid to travel 1 km, considering charging losses
    energy_per_km_kwh = (BATTERY_CAPACITY_KWH / RANGE_KM_PER_CHARGE) / CHARGING_EFFICIENCY
    total_annual_energy_kwh = energy_per_km_kwh * annual_distance_km
    annual_electricity_cost_tl = total_annual_energy_kwh * ELECTRICITY_PRICE_TL_PER_KWH

    print(f"\nEnerji Tüketimi ve Maliyeti:")
    print(f"  Tahmini 1 km başına enerji tüketimi (şarj kaybı dahil): {energy_per_km_kwh:.3f} kWh")
    print(f"  Yıllık toplam enerji tüketimi: {total_annual_energy_kwh:.2f} kWh")
    print(f"  Yıllık elektrik maliyeti: {annual_electricity_cost_tl:.2f} TL") # Illustrates electricity cost calculation

    # 2. Calculate Maintenance Cost
    annual_maintenance_cost_tl = annual_distance_km * MAINTENANCE_COST_PER_KM_TL
    print(f"\nBakım Maliyeti:")
    print(f"  Yıllık bakım maliyeti ({MAINTENANCE_COST_PER_KM_TL:.2f} TL/km): {annual_maintenance_cost_tl:.2f} TL") # Illustrates maintenance cost calculation

    # 3. Calculate Legal Obligations and Spare Parts Cost
    annual_legal_and_parts_cost_tl = ANNUAL_INSURANCE_TL + ANNUAL_MISC_PARTS_TL
    print(f"\nYasal Yükümlülükler ve Yedek Parça Maliyeti:")
    print(f"  Yıllık sigorta/yasal yükümlülük maliyeti: {ANNUAL_INSURANCE_TL:.2f} TL")
    print(f"  Yıllık tahmini yedek parça maliyeti: {ANNUAL_MISC_PARTS_TL:.2f} TL")
    print(f"  Toplam yıllık yasal/yedek parça maliyeti: {annual_legal_and_parts_cost_tl:.2f} TL") # Illustrates legal/parts cost calculation

    # 4. Calculate Total Annual Cost
    total_annual_operating_cost_tl = (
        annual_electricity_cost_tl +
        annual_maintenance_cost_tl +
        annual_legal_and_parts_cost_tl
    )

    print(f"\n--- TOPLAM YILLIK İŞLETME MALİYETİ ---")
    print(f"  Tahmini yıllık kat edilen mesafe: {annual_distance_km} km")
    print(f"  Toplam yıllık işletme maliyeti: {total_annual_operating_cost_tl:.2f} TL")
    print(f"  Kilometre başına maliyet: {total_annual_operating_cost_tl / annual_distance_km:.2f} TL/km")

    return total_annual_operating_cost_tl

if __name__ == "__main__":
    print("Kimi K3 Elektrikli Scooter Yıllık İşletme Maliyeti Hesaplayıcı")
    print("----------------------------------------------------------")

    try:
        user_annual_distance = float(input("Lütfen yıllık tahmini kat edeceğiniz mesafeyi girin (km): "))
        if user_annual_distance <= 0:
            print("Mesafe pozitif bir sayı olmalıdır.")
        else:
            calculate_annual_cost(user_annual_distance)
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
