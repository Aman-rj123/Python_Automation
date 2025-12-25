import psutil

def Server_Data():
    # Get CPU usage over a 1-second interval
    CPU_DATA= psutil.cpu_percent(interval=1)
    
    # Get memory (RAM) usage percentage
    Memory_Data =psutil.virtual_memory().percent
    
    ## Get disk usage percentage
    Disk_Data = psutil.disk_usage('c:\\').percent
    
    """
    Collects system health metrics like CPU, Memory, and Disk usage.

    Returns:
        dict: System usage percentagesgit lll
    """
    
    
    return {
        "CPU (%)" : CPU_DATA,
        "Memory (%)": Memory_Data,
        "Disk (%)": Disk_Data
        
    }
    
print(Server_Data())
    