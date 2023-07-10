/***************************************************************************
 * The contents of this file were generated with Amplify Studio.           *
 * Please refrain from making any modifications to this file.              *
 * Any changes to this file will be overwritten when running amplify pull. *
 **************************************************************************/

import * as React from "react";
import { GridProps } from "@aws-amplify/ui-react";
import { EscapeHatchProps } from "@aws-amplify/ui-react/internal";
export declare type ValidationResponse = {
    hasError: boolean;
    errorMessage?: string;
};
export declare type ValidationFunction<T> = (value: T, validationResponse: ValidationResponse) => ValidationResponse | Promise<ValidationResponse>;
export declare type ProjectInputValues = {};
export declare type ProjectValidationValues = {};
export declare type PrimitiveOverrideProps<T> = Partial<T> & React.DOMAttributes<HTMLDivElement>;
export declare type ProjectOverridesProps = {
    ProjectGrid?: PrimitiveOverrideProps<GridProps>;
} & EscapeHatchProps;
export declare type ProjectProps = React.PropsWithChildren<{
    overrides?: ProjectOverridesProps | undefined | null;
} & {
    onSubmit: (fields: ProjectInputValues) => void;
    onChange?: (fields: ProjectInputValues) => ProjectInputValues;
    onValidate?: ProjectValidationValues;
} & React.CSSProperties>;
export default function Project(props: ProjectProps): React.ReactElement;
