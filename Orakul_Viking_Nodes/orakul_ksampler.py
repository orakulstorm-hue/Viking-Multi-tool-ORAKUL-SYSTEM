import os
import importlib
import folder_paths
import comfy.samplers

class OrakulSamplerSelector:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, {"default": "uni_pc"}),
                "detail_density": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2000000.0, "step": 1.0}),
                "noise_precision": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2000000.0, "step": 1.0}),
                "d_start": ("FLOAT", {"default": 40.0, "min": 0.0, "max": 100.0, "step": 0.1}),
                "d_end": ("FLOAT", {"default": 60.0, "min": 0.0, "max": 100.0, "step": 0.1}),
                "p_start": ("FLOAT", {"default": 85.0, "min": 0.0, "max": 100.0, "step": 0.1}),
                
                "МАНУАЛ_СИСТЕМЫ": ("STRING", {
                    "multiline": True, 
                    "readonly": True,
                    "default": (
                        "╔══════════════════════════════════════════════════════╗\n"
                        "║        ⚔️  СИСТЕМА ORAKUL: БОЕВОЙ УСТАВ  ⚔️         ║\n"
                        "╚══════════════════════════════════════════════════════╝\n\n"
                        "1. МОЩНОСТЬ (ГРАНИЦА ФОЛА) 🛑:\n"
                        "------------------------------------------------------\n"
                        "• DETAIL DENSITY (MAX: 500) 🧱:\n"
                        "  ПОТОЛОК! ВЫШЕ 500 — КАРТИНКА РАЗВАЛИТСЯ.\n\n"
                        "• NOISE PRECISION (MAX: 150,000) 🎯:\n"
                        "  ПРЕДЕЛ! ВЫШЕ 150К — ПОЙДУТ ПИКСЕЛЬНЫЕ ПЯТНА.\n\n"
                        "2. ТАЙМИНГИ (ПРОЦЕНТЫ ШАГОВ) ⏱️:\n"
                        "------------------------------------------------------\n"
                        "• D_START (40%) / D_END (60%)\n"
                        "• P_START (85%)\n\n"
                        "3. СБРОС В СТАНДАРТ (REVERT TO STOCK) ↩️:\n"
                        "------------------------------------------------------\n"
                        "ЕСЛИ ВЫСТАВИТЬ DETAIL И NOISE НА 0.0 — СИСТЕМА\n"
                        "ПЕРЕСТАНЕТ ВНОСИТЬ ПРАВКИ. ВАШ СЭМПЛЕР СТАНЕТ\n"
                        "ОБЫЧНЫМ СТАНДАРТНЫМ UNI_PC БЕЗ ДОП. ДЕТАЛЕЙ.\n\n"
                        "4. ЗОЛОТОЕ ПРАВИЛО ВИКИНГА 🛡️:\n"
                        "------------------------------------------------------\n"
                        "МЕЖДУ 60% И 85% — ПАУЗА (25% ШАГОВ)!\n"
                        "ДАЙТЕ НЕЙРОСЕТИ УСПОКОИТЬ ШУМ ПЕРЕД ФИНИШЕМ.\n\n"
                        "⚠️ ВСЁ, ЧТО ВЫШЕ 500 / 150к — НА ВАШ СТРАХ И РИСК ☠️\n"
                        "______________________________________________________"
                    )
                }),
            }
        }

    RETURN_TYPES = ("SAMPLER",)
    RETURN_NAMES = ("SAMPLER",)
    FUNCTION = "ignite"
    CATEGORY = "Viking_Nodes"

    def ignite(self, sampler_name, detail_density, noise_precision, d_start, d_end, p_start, **kwargs):
        d_num = float(detail_density)
        p_num = float(noise_precision)
        
        # ТВОИ МНОЖИТЕЛИ
        final_d = format(0.00001 * d_num, ".10f").rstrip('0').rstrip('.')
        final_p = format(0.000001 * p_num, ".10f").rstrip('0').rstrip('.')
        
        # КОНВЕРТАЦИЯ ПРОЦЕНТОВ
        ds = format(d_start / 100.0, ".2f")
        de = format(d_end / 100.0, ".2f")
        ps = format(p_start / 100.0, ".2f")

        file_path = os.path.join(folder_paths.base_path, "comfy", "extra_samplers", "uni_pc.py")

        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            new_lines = []
            for line in lines:
                if "[ORAKUL_D_RANGE]" in line:
                    indent = line[:line.find("if ")]
                    new_lines.append(f"{indent}if {ds} <= ratio <= {de}: # [ORAKUL_D_RANGE]\n")
                elif "[ORAKUL_P_START]" in line:
                    indent = line[:line.find("if ")]
                    new_lines.append(f"{indent}if ratio > {ps}: # [ORAKUL_P_START]\n")
                elif "[ORAKUL_D]" in line:
                    indent = line[:line.find("x.add_")]
                    new_lines.append(f"{indent}x.add_(torch.randn_like(x) * {final_d} * 1)# [ORAKUL_D]\n")
                elif "[ORAKUL_P]" in line:
                    indent = line[:line.find("x.add_")]
                    new_lines.append(f"{indent}x.add_(torch.randn_like(x) * {final_p} * 1)# [ORAKUL_P]\n")
                else:
                    new_lines.append(line)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)

            # --- ТВОЙ РОДНОЙ ТЕРМИНАЛ (ВОССТАНОВЛЕН) ---
            mode = "CUSTOM"
            if d_num == 0 and p_num == 0: mode = "🏁STANDARD🏁"
            elif 0 < p_num <= 50000: mode = "👩‍🎨STOCK (На пути к шедеврам)👨‍🎨"
            elif 50000 < p_num <= 80000: mode = "👨‍🔧HIGH TEXTURE (Уплотняем текстуру)👨‍🔧"
            elif 80000 < p_num <= 100000: mode = "🚧Sculpting mode (АГРЕССИЯ)🚧"
            elif 100000 < p_num <= 150000: mode = "📈LIMIT BREAK (МАКСИМУМ)📈"
            elif p_num > 150000: mode = "⚠️!!!🚀WOW🚀!!!⚠️ (ты выходишь за пределы фантазии, далее только шум,  хотя...🤔🧐)"
            
            importlib.reload(importlib.import_module("comfy.extra_samplers.uni_pc"))
            
            print("\n" + "⚔️ " * 40)
            print(f"   [ORAKUL SYSTEM ACTIVE]")
            print(f"   MODE: {mode}")
            print(f"   DENSITY: {detail_density} (sys: {final_d})")
            print(f"   PRECISION: {noise_precision} (sys: {final_p})")
            print(f"   TIMING: D({d_start}%-{d_end}%) | P({p_start}%)")
            print("⚔️ " * 40 + "\n")
            # ------------------------------------------

        return (comfy.samplers.sampler_object(sampler_name),)

NODE_CLASS_MAPPINGS = {"OrakulSamplerSelector": OrakulSamplerSelector}
NODE_DISPLAY_NAME_MAPPINGS = {"OrakulSamplerSelector": "🚀 ORAKUL SYSTEM SELECTOR  👨‍🔧Multitool👨‍🔧"}