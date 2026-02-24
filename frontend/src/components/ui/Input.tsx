"use client";

import { forwardRef, type InputHTMLAttributes } from "react";

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ label, error, className = "", id, ...props }, ref) => {
    const inputId = id || label?.toLowerCase().replace(/\s+/g, "-");

    return (
      <div className="w-full">
        {label && (
          <label
            htmlFor={inputId}
            className="block text-sm font-medium text-text mb-1.5"
          >
            {label}
          </label>
        )}
        <input
          ref={ref}
          id={inputId}
          className={[
            "w-full h-10 px-3 rounded-[var(--radius-lg)]",
            "border bg-surface text-text placeholder:text-text-muted",
            "focus:outline-2 focus:outline-offset-0 focus:outline-indigo",
            error
              ? "border-rose focus:outline-rose"
              : "border-glass-border",
            className,
          ].join(" ")}
          {...props}
        />
        {error && (
          <p className="mt-1 text-sm text-rose">{error}</p>
        )}
      </div>
    );
  },
);

Input.displayName = "Input";
export { Input };
export type { InputProps };
