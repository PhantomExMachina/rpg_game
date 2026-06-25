def restore_health_full(target, current_health, max_health):
    if target:
        target.current_health = max_health
