# Adapted from OSU-NLP-Group/TravelPlanner utils/budget_estimation.py
# MIT License - Copyright (c) 2024 OSU Natural Language Processing
# Permission notice included per MIT terms. See upstream LICENSE.
# SAFETY NOTE: Upstream budget_calc uses unsafe dynamic code execution on external distance-matrix data. That function was NOT copied verbatim. If reimplemented, parse cost safely with float conversion instead.

def estimate_budget(data, mode):
    clean = [x for x in data if str(x) != 'nan']
    if mode == 'lowest':
        return min(clean)
    elif mode == 'highest':
        return max(clean)
    elif mode == 'average':
        return sum(clean) / len(clean)
    raise ValueError('mode must be lowest, highest, or average')
