"""
Savunma Sanayii Tedarik ve Lojistik Süreçleri İçin Akıllı Rota Optimizasyonu
Problem: Kapasiteli Araç Rotalama Problemi (Capacitated Vehicle Routing Problem - CVRP)
Yaklaşım: Sezgisel Arama & Karar Destek Algoritması
"""

import math
import matplotlib.pyplot as plt

# 1. PARAMETRELER VE VERİ SETİ
# Ana Lojistik Üssü (Depot) ve İkmal Noktaları (Nodes)
DEPOT = {"id": 0, "name": "Ana Lojistik Üssü", "x": 50, "y": 50}

NODES = [
    {"id": 1, "name": "Üs Bölgesi A", "x": 20, "y": 80, "demand": 15},
    {"id": 2, "name": "Üs Bölgesi B", "x": 35, "y": 90, "demand": 20},
    {"id": 3, "name": "Gözetleme Noktası 1", "x": 80, "y": 85, "demand": 10},
    {"id": 4, "name": "Radar İstasyonu", "x": 90, "y": 40, "demand": 25},
    {"id": 5, "name": "İleri Karakol 1", "x": 70, "y": 15, "demand": 30},
    {"id": 6, "name": "İleri Karakol 2", "x": 30, "y": 20, "demand": 15},
    {"id": 7, "name": "Hava Savunma Bataryası", "x": 15, "y": 45, "demand": 20},
    {"id": 8, "name": "İkmal Destek Noktası", "x": 60, "y": 65, "demand": 10}
]

VEHICLE_CAPACITY = 45  # Bir aracın taşıyabileceği maksimum yük kapasitesi

# 2. ÖKLİD MESAFESİ HESAPLAMA FONKSİYONU
def calculate_distance(p1, p2):
    return math.sqrt((p1["x"] - p2["x"])**2 + (p1["y"] - p2["y"])**2)

# 3. SEZGİSEL ROTA OLUŞTURMA ALGORİTMASI (Heuristic Routing)
def solve_routing():
    unvisited = NODES.copy()
    routes = []
    
    while unvisited:
        current_route = []
        current_load = 0
        current_node = DEPOT
        
        while unvisited:
            feasible_nodes = [node for node in unvisited if current_load + node["demand"] <= VEHICLE_CAPACITY]
            if not feasible_nodes:
                break
                
            next_node = min(feasible_nodes, key=lambda n: calculate_distance(current_node, n))
            current_route.append(next_node)
            current_load += next_node["demand"]
            unvisited.remove(next_node)
            current_node = next_node
            
        routes.append(current_route)
        
    return routes

# 4. METRİK VE MALİYET ANALİZİ
def print_optimization_summary(routes):
    total_distance = 0
    print("=== SAVUNMA LOJİSTİĞİ ROTA OPTİMİZASYONU SONUÇLARI ===")
    for i, route in enumerate(routes, 1):
        dist = 0
        current = DEPOT
        route_names = [DEPOT["name"]]
        
        for node in route:
            dist += calculate_distance(current, node)
            current = node
            route_names.append(node["name"])
            
        dist += calculate_distance(current, DEPOT)
        route_names.append(DEPOT["name"])
        total_distance += dist
        
        load = sum(n["demand"] for n in route)
        print(f"Rota {i}: {' -> '.join(route_names)}")
        print(f"   Kapasite Doluluğu: {load}/{VEHICLE_CAPACITY} birim | Rota Uzunluğu: {dist:.2f} km\n")
        
    print(f"Toplam Kat Edilen Mesafe: {total_distance:.2f} km")
    print(f"Görevlendirilen Toplam Araç Sayısı: {len(routes)}")

if __name__ == "__main__":
    optimized_routes = solve_routing()
    print_optimization_summary(optimized_routes)
