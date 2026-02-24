interface ProgressProps {
  value: number;
  label?: string;
  className?: string;
}

export function Progress({ value, label, className = "" }: ProgressProps) {
  const clamped = Math.max(0, Math.min(100, value));

  return (
    <div className={`w-full ${className}`}>
      {label && (
        <div className="flex items-center justify-between mb-1.5">
          <span className="text-sm text-text-dim">{label}</span>
          <span className="text-sm font-medium text-text">{clamped}%</span>
        </div>
      )}
      <div className="h-2 w-full rounded-full bg-surface-light overflow-hidden">
        <div
          className="h-full rounded-full bg-indigo transition-all duration-500 ease-out"
          style={{ width: `${clamped}%` }}
        />
      </div>
    </div>
  );
}
