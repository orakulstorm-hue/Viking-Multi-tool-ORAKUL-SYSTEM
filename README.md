# Viking Multi-tool: ORAKUL SYSTEM
### Advanced Latent Density Controller for Diffusion Models (Flux, SDXL, SD1.5)

**Node Name in UI:** `🚀 ORAKUL SYSTEM SELECTOR  👨‍🔧MULTITOOL👨‍🔧`

> **TECHNICAL NOTE:** Все изображения и видео в этой статье — это прямые скриншоты и записи оригинальных генераций. 
> **Zero Post-Processing.** Без фотошопа и внешних апскейлеров. Вы видите чистую математику метода.

## ⚡ The Viking Method: Why Our Scheduler?
While our initial R&D was conducted using the **Beta Sampler**, we **strongly recommend** using our custom **Viking Scheduler**. 

### 🍣 Beta Sampler vs ORAKUL (Side-by-Side)
На видео ниже показана разница в реальном времени. Обратите внимание, как структура кадра обретает вес и плотность.
<video src="demo.mp4" controls="controls" style="max-width: 100%;"></video>


https://github.com/user-attachments/assets/9a512504-d5c8-48b0-864e-c506c51addf8


---

## 🛠 ORAKUL SYSTEM: The Power of Viking Scheduler
Наш шедулер открывает истинную ДНК изображения, работая с высокоплотными векторами без «цифровой пыли».

### Visual Proof: The Infinite Pupil
![Viking Stock](viking_stock.jpg)
*Stock (500/50k): Нативная влажность и микро-рельеф, недоступные стандартным сэмплерам.*

![Viking Extreme](viking_extreme.jpg)
*Extreme (10k/80k): Бесконечная глубина зрачка. Вглядитесь в отражение — данные не заканчиваются.*

## ⚙️ Parameters & Calibration
| Level | Detail Density (DTL) | Noise Precision (NP) | Description |
| :--- | :--- | :--- | :--- |
| **Minimum** | 0 | 0 | Native model weights. No intervention. |
| **Stock (Recommended)** | **500** | **50,000** | The "Golden Standard". Razor-sharp reality. |
| **Extreme** | 10,000 | 80,000+ | Hyper-reality. Extreme data density. |

## ⚠️ The Golden Rule: The 25% Buffer
* **Instruction:** Always leave the last **20% to 25%** of steps for the model's native weights to balance the final output.
* **Result:** This ensures a "clean finish" without halos or artifacts.

## 🖥 Terminal Transparency
![Terminal Log](terminal.jpg)
*Мы выводим реальную математику в лог. Вы видите статус системы и значения `sys` в реальном времени.*

## 🧬 Logic Inside
Мы не просто добавили ползунки. Мы переписали логику взаимодействия шума с весами на каждом шаге. Если вы хотите увидеть математику этого процесса — загляните в исходный код. **Там всё честно.**

## 📥 Installation / Установка
1. **Custom Node:** Перенесите папку `viking_multitool` в:  
   `Packages\ComfyUI\custom_nodes\`
2. **Custom Sampler:** Перенесите наш файл `nodes_custom_sampler.py` (с заменой оригинального) в:  
   `Packages\ComfyUI\comfy_extras\`  
   *(ВАЖНО: Обязательно сохраните копию оригинального файла перед заменой).*

---
*Developed in the shadows. Tested on RTX 4090. Zero BS.*
